from django.shortcuts import render


def marketplace_home(request):
    return render(request, 'home/index.html', {})