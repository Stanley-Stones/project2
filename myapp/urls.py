from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('property_create/', views.create, name = 'property_create'),
    path('property_details/<str:pk>/', views.details, name = 'property_details'),
    path('property_update/<str:pk>/', views.update, name = 'property_update'),
    path('property_delete/<str:pk>/', views.delete, name = 'property_delete'),

    path('search_property/', views.search, name = 'search'),

    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
]
