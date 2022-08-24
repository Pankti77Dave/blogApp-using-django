from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:tag_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.tag, name='tag_detail'),
]