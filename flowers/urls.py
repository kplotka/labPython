from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('slownik/', views.dictionary, name='dictionary'),
    path('planer/', views.planner, name='planner'),
    path('add-to-bouquet/', views.add_to_bouquet, name='add_to_bouquet'),
    path('bukiet/', views.bouquet, name='bouquet'),
    path('usun-z-bukietu/<int:flower_id>/', views.remove_from_bouquet, name='remove_from_bouquet'),
    path('wyczysc-bukiet/', views.clear_bouquet, name='clear_bouquet'),
    path('zapisz-bukiet/', views.save_bouquet, name='save_bouquet'),
    path('moje-bukiety/', views.my_bouquets, name='my_bouquets'),
    path('zapisz-bukiet/', views.save_bouquet, name='save_bouquet'),
    path('usun-bukiet/<int:bouquet_id>/', views.delete_bouquet, name='delete_bouquet'),
    path('wyczysc-bukiet/', views.clear_bouquet, name='clear_bouquet'),
    path('zaladuj-bukiet/<int:bouquet_id>/', views.load_bouquet, name='load_bouquet'),
]