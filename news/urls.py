"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from main import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('', views.get_home, name='get_home'),
    path('sources_list/', views.get_sources_list, name='get_sources_list'),
    path('sources_table/', views.get_sources_table, name='get_sources_table'),
    path('source/create/', views.create_source),
    path('source/stats/', views.get_stats, name='get_stats'),
    path('source/<int:pk>', views.get_source, name='get_source'),
    path('resources_ik', views.get_resources_ik, name='get_resources_ik')

]
