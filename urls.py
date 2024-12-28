
from django.urls import path
from . import views

urlpatterns = [
    path('add_review/', views.add_review, name='add_review'),
    path('display_reviews/', views.display_reviews, name='display_reviews'),
    path('display_reviews/', views.display_reviews, name='display_reviews'),
]
