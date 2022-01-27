from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.http import response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import action
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Partner


# Create your views here.

class AuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path="register", url_name="register")
    def register(self, request, *args, **kwargs):
        return Response(self.request.data)
    
    @action(detail=False, methods=['post'], url_path="generate-token", url_name="generate-token")
    def generate_token(self, request, *args, **kwargs):
        return Response(self.request.data)
    

class PartnerRegisterView(TemplateView):
    """
    View to register a partner
    """
    template_name = "auth_handler/partner_register.html"

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = User.objects.get_or_create(email=data['email'], username=data['email'])[0]
        user.set_password(data['password'])
        user.save()
        
        login(request, user)

        partner = Partner.objects.create(
            user = user,
            partner_name = data['partner_name'],
            partner_desc = data['partner_desc']
        )
        return redirect('marketplace_api_auth_handler:register_successful')


class SuccessfulPartnerRegisterView(View):
    """
    Successful registration page view
    """

    def get(self, request):
        data ={}
        try:
            token = Token.objects.get_or_create(user=request.user)[0]
            data['token'] = token
        except:
            pass
        return render(request, 'auth_handler/successful_partner_registration.html', data)


