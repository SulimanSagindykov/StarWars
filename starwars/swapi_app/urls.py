from django.urls import path
from .views import get_characters

urlpatterns = [
    path('characters/', get_characters, name='get-characters'),
]