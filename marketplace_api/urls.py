from django.urls import path, include
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('', include('marketplace_api.home.urls')),
    path('auth/', include('marketplace_api.auth_handler.urls')),

    # APIs
    path('api/recommendation/', include('marketplace_api.recommendation.urls')),
]