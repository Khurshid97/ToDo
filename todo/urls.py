"""owner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import path
from . import views
from .models import *

urlpatterns = [
    # in the views file we can find home function where we do some operations
    path('', views.home, name='home'),
    path('create/', views.createFormView, name='create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
] 