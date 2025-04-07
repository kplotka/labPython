from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CastingOffer, ModelProfile, DirectorProfile, Application
from .forms import CastingOfferForm, ApplicationForm, CustomUserCreationForm, ModelProfileForm, DirectorProfileForm

def home(request):
    return render(request, 'casting/home.html')

@login_required
def add_casting_offer(request):
    try:
        director_profile = request.user.director_profile
    except DirectorProfile.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        form = CastingOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.director = director_profile
            offer.save()
            return redirect('offers_list')
    else:
        form = CastingOfferForm()
    return render(request, 'casting/add_casting_offer.html', {'form': form})

def offers_list(request):
    offers = CastingOffer.objects.all().order_by('-created_at')
    applied_offer_ids = []
    if hasattr(request.user, 'model_profile'):
        applied_offer_ids = Application.objects.filter(model_profile=request.user.model_profile).values_list('offer_id', flat=True)
    return render(request, 'casting/offers_list.html', {
        'offers': offers,
        'applied_offer_ids': list(applied_offer_ids)
    })

def offer_detail(request, offer_id):
    offer = get_object_or_404(CastingOffer, id=offer_id)
    already_applied = False
    if hasattr(request.user, 'model_profile'):
        if offer.applications.filter(model_profile=request.user.model_profile).exists():
            already_applied = True
    return render(request, 'casting/offer_detail.html', {
        'offer': offer,
        'already_applied': already_applied,
    })

@login_required
def apply_offer(request, offer_id):
    offer = get_object_or_404(CastingOffer, id=offer_id)
    try:
        model_profile = request.user.model_profile
    except ModelProfile.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.offer = offer
            application.model_profile = model_profile
            application.save()
            return redirect('offer_detail', offer_id=offer.id)
    else:
        form = ApplicationForm()
    return render(request, 'casting/apply_offer.html', {'form': form, 'offer': offer})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            if role == 'model':
                ModelProfile.objects.create(user=user, full_name=user.username)
            elif role == 'director':
                DirectorProfile.objects.create(user=user, full_name=user.username)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'casting/register.html', {'form': form})

@login_required
def profile(request):
    try:
        model_profile = request.user.model_profile
        applications = model_profile.applications.all().order_by('-applied_at')
        return render(request, 'casting/model_profile.html', {
            'profile': model_profile,
            'applications': applications
        })
    except ModelProfile.DoesNotExist:
        try:
            director_profile = request.user.director_profile
            offers = director_profile.casting_offers.all().order_by('-created_at')
            offers_with_counts = [(offer, offer.applications.count()) for offer in offers]
            return render(request, 'casting/director_profile.html', {
                'profile': director_profile,
                'offers_with_counts': offers_with_counts
            })
        except DirectorProfile.DoesNotExist:
            return redirect('home')

@login_required
def edit_profile(request):
    try:
        director_profile = request.user.director_profile
        profile_type = 'director'
    except DirectorProfile.DoesNotExist:
        director_profile = None
        profile_type = None
    if not profile_type:
        try:
            model_profile = request.user.model_profile
            profile_type = 'model'
        except ModelProfile.DoesNotExist:
            return redirect('home')
    if profile_type == 'director':
        if request.method == 'POST':
            form = DirectorProfileForm(request.POST, request.FILES, instance=director_profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = DirectorProfileForm(instance=director_profile)
    else:
        if request.method == 'POST':
            form = ModelProfileForm(request.POST, request.FILES, instance=model_profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ModelProfileForm(instance=model_profile)
    return render(request, 'casting/edit_profile.html', {'form': form})

@login_required
def edit_offer(request, offer_id):
    try:
        director_profile = request.user.director_profile
    except DirectorProfile.DoesNotExist:
        return redirect('home')
    offer = get_object_or_404(CastingOffer, id=offer_id, director=director_profile)
    if request.method == 'POST':
        form = CastingOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CastingOfferForm(instance=offer)
    return render(request, 'casting/edit_offer.html', {'form': form, 'offer': offer})

@login_required
def delete_offer(request, offer_id):
    try:
        director_profile = request.user.director_profile
    except DirectorProfile.DoesNotExist:
        return redirect('home')
    offer = get_object_or_404(CastingOffer, id=offer_id, director=director_profile)
    if request.method == "POST":
        offer.delete()
        return redirect('profile')
    return render(request, 'casting/delete_offer_confirm.html', {'offer': offer})

@login_required
def view_applications(request, offer_id):
    offer = get_object_or_404(CastingOffer, id=offer_id)
    try:
        director_profile = request.user.director_profile
    except DirectorProfile.DoesNotExist:
        return redirect('home')
    if offer.director != director_profile:
        return redirect('home')
    applications = offer.applications.all().order_by('-applied_at')
    return render(request, 'casting/manage_applications.html', {
        'offer': offer,
        'applications': applications
    })

@login_required
def update_application_status(request, application_id, new_status):
    application = get_object_or_404(Application, id=application_id)
    try:
        director_profile = request.user.director_profile
    except DirectorProfile.DoesNotExist:
        return redirect('home')
    if application.offer.director != director_profile:
        return redirect('home')
    if request.method == 'POST':
        application.status = new_status
        application.save()
        return redirect('view_applications', offer_id=application.offer.id)
    return render(request, 'casting/update_application_status.html', {'application': application, 'new_status': new_status})

@login_required
def model_profile_detail(request, profile_id):
    from django.shortcuts import get_object_or_404
    profile = get_object_or_404(ModelProfile, id=profile_id)
    try:
        director_profile = request.user.director_profile
    except DirectorProfile.DoesNotExist:
        return redirect('home')
    return render(request, 'casting/model_profile_detail.html', {'profile': profile})