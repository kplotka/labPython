import random
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Flower, Category, SavedBouquet


def home(request):
    return render(request, 'home.html')


def dictionary(request):
    flowers = Flower.objects.all().order_by('name')
    return render(request, 'dictionary.html', {'flowers': flowers})


def planner(request):
    categories = Category.objects.all()
    selected_ids = request.GET.getlist('category')
    if selected_ids:
        flowers = Flower.objects.filter(categories__id__in=selected_ids).distinct()
    else:
        flowers = Flower.objects.all()

    return render(request, 'planner.html', {
        'flowers': flowers,
        'categories': categories,
        'selected_ids': list(map(int, selected_ids)),
    })


def add_to_bouquet(request):
    flower_id = request.POST.get('flower_id')
    if not flower_id:
        return JsonResponse({'error': 'Brak ID kwiatka'}, status=400)
    try:
        flower_id = int(flower_id)
    except ValueError:
        return JsonResponse({'error': 'Nieprawidłowe ID'}, status=400)

    bouquet = request.session.get('bouquet', [])
    if flower_id not in bouquet:
        bouquet.append(flower_id)
        request.session['bouquet'] = bouquet
        request.session.modified = True

    return JsonResponse({'message': 'Dodano do bukietu!'})


@require_POST
def remove_from_bouquet(request):
    flower_id = request.POST.get('flower_id')
    try:
        flower_id = int(flower_id)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Nieprawidłowe ID'}, status=400)

    bouquet = request.session.get('bouquet', [])
    bouquet = [int(f) for f in bouquet if int(f) != flower_id]
    request.session['bouquet'] = bouquet
    request.session.modified = True

    return JsonResponse({'message': 'Usunięto z bukietu'})


@require_POST
def clear_bouquet(request):
    request.session['bouquet'] = []
    request.session.modified = True
    return JsonResponse({'message': 'Bukiet wyczyszczony'})


def bouquet(request):
    bouquet_ids = request.session.get('bouquet', [])
    bouquet_ids = [int(i) for i in bouquet_ids if str(i).isdigit()]
    flowers = Flower.objects.filter(id__in=bouquet_ids)

    bouquet_data = []
    for flower in flowers:
        rotation = random.randint(-10, 10)
        bouquet_data.append((flower, rotation))

    return render(request, 'bouquet.html', {'bouquet': bouquet_data})

@require_POST
@login_required
def save_bouquet(request):
    name = request.POST.get("name", "").strip()
    bouquet_ids = request.session.get('bouquet', [])
    bouquet_ids = [int(i) for i in bouquet_ids if str(i).isdigit()]
    flowers = Flower.objects.filter(id__in=bouquet_ids)

    if not name:
        return JsonResponse({'error': 'Podaj nazwę bukietu'}, status=400)

    if flowers.exists():
        bouquet = SavedBouquet.objects.create(user=request.user, name=name)
        bouquet.flowers.set(flowers)
        return JsonResponse({'message': 'Bukiet zapisany!'})
    return JsonResponse({'error': 'Bukiet jest pusty'}, status=400)

@login_required
def my_bouquets(request):
    bouquets = SavedBouquet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_bouquets.html', {'bouquets': bouquets})

@require_POST
@login_required
def delete_bouquet(request, bouquet_id):
    try:
        bouquet = SavedBouquet.objects.get(id=bouquet_id, user=request.user)
        bouquet.delete()
        return JsonResponse({'message': 'Bukiet usunięty'})
    except SavedBouquet.DoesNotExist:
        return JsonResponse({'error': 'Nie znaleziono bukietu'}, status=404)

def clear_bouquet(request):
    request.session['bouquet'] = []
    request.session.modified = True
    return JsonResponse({'message': 'Bukiet wyczyszczony'})
