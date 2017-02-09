from django.shortcuts import render
from django.utils import timezone
from .models import Color

def color_list(request):
    colors = Color.objects.all()
    return render(request, 'color_library/color_list.html', {'colors': colors})
