from django.urls import path
from .views import  CustomerList
from .views import RegisterUserView, LoginUserView

urlpatterns = [
    path('posts/', CustomerList.as_view(), name='get-list-create'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'), 
]