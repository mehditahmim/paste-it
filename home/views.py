from django.shortcuts import render
from paste.models import Paste

def index(request):
    
    latest_paste = Paste.objects.order_by('-created_at')[:5]
    return render(request, 'home/home.html',{'latest_paste':latest_paste})
    

# Create your views here.
