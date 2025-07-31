from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>home view</p>')

def pet_detail(request, pet_id):
    return HttpResponse(f'<p>Pet detail view for pet ID: {pet_id}</p>')