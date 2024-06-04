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
    path('soups/<int:soup_id>/add_meal/', views.add_meal, name='add_meal'),
    path('ingredients/', views.ing_index, name='ing_index'),
    path('ingredients/<int:ing_id>/', views.ing_detail, name='ing_detail'),
    path('ingredients/create', views.ing_create.as_view(), name='add_ing'),
    path('ingredients/<int:pk>/edit/', views.ing_edit.as_view(), name='edit_ing'),
    path('ingredients/<int:pk>/delete/', views.ing_delete.as_view(), name='del_ing')
]