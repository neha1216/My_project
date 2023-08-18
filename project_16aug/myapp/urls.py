from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    # path('log',views.login, name = 'log'),
    path('login', views.loginn, name='login'),
]