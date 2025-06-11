import random
from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Flower, Category, SavedBouquet


def home(request):
    return render(request, 'home.html')


def dictionary(request):
    flowers = Flower.objects.all().order_by('name')
    grouped_flowers = defaultdict(list)

    for flower in flowers:
        first_letter = flower.name[0].upper()
        grouped_flowers[first_letter].append(flower)

    grouped_flowers = dict(sorted(grouped_flowers.items()))

    return render(request, 'dictionary.html', {
        'grouped_flowers': grouped_flowers
    })

def planner(request):
    all_categories = Category.objects.all()
    selected_categories = request.GET.getlist('category')

    if selected_categories:
        flowers = Flower.objects.filter(categories__name__in=selected_categories).distinct()
    else:
        flowers = Flower.objects.all()

    message = request.GET.get("message", "")

    return render(request, 'planner.html', {
        'flowers': flowers,
        'all_categories': all_categories,
        'selected_categories': selected_categories,
        'message': message,
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

    params = urlencode({'message': 'Dodano do bukietu'})
    return redirect(f"/planer/?{params}")

def remove_from_bouquet(request, flower_id):
    if request.method == 'POST':
        bouquet = request.session.get('bouquet', [])
        bouquet = [fid for fid in bouquet if str(fid) != str(flower_id)]
        request.session['bouquet'] = bouquet
        request.session.modified = True
        return redirect('bouquet')


def clear_bouquet(request):
    if request.method == 'POST':
        request.session['bouquet'] = []
        request.session.modified = True
        return redirect('bouquet')

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

@login_required
def load_bouquet(request, bouquet_id):
    if request.method == 'POST':
        bouquet = get_object_or_404(SavedBouquet, id=bouquet_id, user=request.user)
        request.session['bouquet'] = [flower.id for flower in bouquet.flowers.all()]
        request.session.modified = True
        return redirect('bouquet')