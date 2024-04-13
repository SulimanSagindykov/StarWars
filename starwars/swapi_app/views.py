from django.shortcuts import render

# Create your views here.

import requests
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache

@cache_page(60 * 15)  # Cache for 15 minutes
def get_characters(request):
    try:
        response = requests.get('https://swapi.dev/api/people/')
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return JsonResponse(data)
    except requests.RequestException as e:
        # Log the error or handle it appropriately
        return JsonResponse({'error': 'Failed to fetch data from SWAPI'}, status=500)