from django.urls import path
from .views import  CustomerList
from .views import RegisterUserView, LoginUserView, GetAllUserListView, ChangePasswordView , LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'), 
    path('userlist/', GetAllUserListView.as_view(), name='get-user-list'), 
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
]