"""
URL configuration for cactus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from main import views

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name= 'index'),
    path('corzina/', views.corzina , name= 'corzina'),
    path('carta/' , views.carta , name= 'carta'),
    path('logreg/' , views.logreg , name='logreg')
]
