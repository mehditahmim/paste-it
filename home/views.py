from django.shortcuts import render


def index(request):
   
    return render(request, 'home/home.html')
    

# Create your views here.
