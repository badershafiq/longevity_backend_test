from django.urls import path, include
from django.contrib.auth import logout

from marketplace_api.auth_handler.views import PartnerRegisterView, SuccessfulPartnerRegisterView
from rest_framework.routers import DefaultRouter

app_name = 'marketplace_api_auth_handler'


urlpatterns = [
    path('register/', PartnerRegisterView.as_view(), name='register'),
    path('register/successful/', SuccessfulPartnerRegisterView.as_view(), name='register_successful'),
    path('logout/', logout, name='logout'),
]
