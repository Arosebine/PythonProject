from django.urls import path, include
from backend import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('register-page/', views.register, name='register'),
]
