from django.contrib import admin
from django.urls import path
from pages.views import Users_list_view, user_profile_view, sign_in_view, dynamic_view, user_delete_view

app_name = 'pages'

urlpatterns = [
    path('profile', user_profile_view, name='profile'),
    path('', sign_in_view, name="signin"),
    path('<int:my_id>/', dynamic_view, name="sign"),
    path('<int:my_id>/delete/', user_delete_view, name="delete-user"),
    path('users/', Users_list_view, name="Users-list")
]