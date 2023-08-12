from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(request, 'index.html')

def top_sellers(request):
    return render (request, 'top_sellers.html')