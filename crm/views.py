from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "crm/home_page.html")
