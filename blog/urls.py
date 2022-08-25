
from django.urls import path
from . import views



urlpatterns = [
    path('search/', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('<int:id>/', views.detail, name='post_detail'),
    # path('<slug:slug>/', views.tag, name='tag_detail'),
] 