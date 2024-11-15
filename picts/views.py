from django.shortcuts import render
from django.utils import timezone
from .models import Fotos

# Create your views here.
def post_list(request):
    return render(request, 'picts/Fotos_list.html', {})