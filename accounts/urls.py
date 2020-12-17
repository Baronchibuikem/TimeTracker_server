from django.urls import path
from accounts.views import user_signup, user_login, user_logout, user_edit_profile
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('signup/', user_signup, name="signup"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('edit-profile/', user_edit_profile, name="edit-profile")
]
