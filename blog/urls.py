from django.urls import path

from . import views

urlpatterns = [
    path('<slug:tag_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.tag, name='tag_detail'),
]