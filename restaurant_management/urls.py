
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.api_home, name='home'), 
    path('api/auth/', include('accounts.urls')),
    path('api/', include('restaurant.urls')),
]
