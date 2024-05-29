from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('soups/', views.soup_index, name='index'),
    path('soups/<int:soup_id>/', views.soup_detail, name='detail'),
]