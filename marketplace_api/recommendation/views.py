import json

from django.shortcuts import render
from rest_framework import viewsets, status, response, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .recommendation_engine import RecommendationEngine

# Create your views here.
class RecommendationViewset(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    """
    Third-party recommendation service

    POST request object
        {
            "param_1": "value_1",
            ...
            "param_N": "value_N",
        }
    """
    def create(self, request, *args, ** kwargs):
        engine = RecommendationEngine()
        data = engine.get_recommendation()
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["post"], url_path="internal", url_name="internal")
    def internal_recommendation_service(self, request, *args, **kwargs):
        """
        Internal recommendation service
        """
        engine = RecommendationEngine()
        data = engine.get_recommendation()
        return Response(data, status=status.HTTP_200_OK)
