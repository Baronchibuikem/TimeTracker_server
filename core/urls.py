from django.urls import path
from core.views import frontpage, privacy, terms_of_service, plans, myaccount


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('privacy/', privacy, name="privacy"),
    path('terms/', terms_of_service, name="terms"),
    path('plans/', plans, name="plans"),
    path('myaccount/', myaccount, name="myaccount")

]
