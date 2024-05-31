from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('soups/', views.soup_index, name='index'),
    path('soups/<int:soup_id>/', views.soup_detail, name='detail'),
    path('soups/create/', views.soup_create.as_view(), name='add_soup'),
    path('soups/<int:pk>/update/', views.soup_update.as_view(), name='update_soup'),
    path('soups/<int:pk>/delete/', views.soup_delete.as_view(), name='delete_soup'),
]