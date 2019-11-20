from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBackend.as_view()),
    path('<int:pk>/', views.DetailBackend.as_view()),
]