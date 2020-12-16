from django.urls import path
from accounts.views import signup

app_name = "accounts"

urlpatterns = [
    path('', signup, name="signup"),
    # path('privacy/',privacy, name="privacy"),
    # path('terms/', terms_of_service, name="terms"),
    # path('plans/', plans, name="plans")

]
