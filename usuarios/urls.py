from django.urls import path
from .views import register_user, login_user, get_all_roles, get_byid_user,get_all_users

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('roles/', get_all_roles, name="get_all_roles"),
    path('users', get_all_users, name="get_all_users"),
    path('user/<int:user_id>', get_byid_user, name="get_byid_user")
]