from django.urls import path
from marketplace_api.home import views

app_name = 'marketplace_api_home'

urlpatterns = [
    path('', views.marketplace_home, name='home')
]
