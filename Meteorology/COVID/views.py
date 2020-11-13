from django.shortcuts import render
from .Process import Process as process
from django.http import HttpResponse, JsonResponse

# Create your views here.


def Index(request):
    new_process = process.Process()

    return JsonResponse({'keys': str(new_process.get_keys())})