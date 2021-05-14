from django.shortcuts import render
from paste.models import Paste

def index(request):
    
    pastes = Paste.objects.all().order_by('-created_at')[:5]
    ctx = {}
    ctx['header'] = ['Author','Title','Date']
    ctx['pastes'] = pastes
    return render(request, 'home/home.html',ctx)
    

# Create your views here.
