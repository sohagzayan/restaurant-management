from django.shortcuts import render
from django.conf import settings


def api_home(request):
    context = {
        'base_url': settings.BASE_URL  
    }
    return render(request, 'template.html', context)

