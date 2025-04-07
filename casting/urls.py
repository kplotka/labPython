from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-offer/', views.add_casting_offer, name='add_casting_offer'),
    path('offers/', views.offers_list, name='offers_list'),
    path('offer/<int:offer_id>/', views.offer_detail, name='offer_detail'),
    path('offer/<int:offer_id>/apply/', views.apply_offer, name='apply_offer'),
    path('offer/<int:offer_id>/edit/', views.edit_offer, name='edit_offer'),
    path('offer/<int:offer_id>/delete/', views.delete_offer, name='delete_offer'),
    path('offer/<int:offer_id>/applications/', views.view_applications, name='view_applications'),
    path('application/<int:application_id>/update/<str:new_status>/', views.update_application_status, name='update_application_status'),
    path('model-profile/<int:profile_id>/', views.model_profile_detail, name='model_profile_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='casting/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]