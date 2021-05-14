from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from django.urls.base import reverse
from .forms import CreatePasteForm,EditPasteForm
from django.contrib.auth.models import User
from .models import  Paste
# Create your views here.

def createPaste(request):
    # This view is responsible for creating new paste
    if request.method == 'POST':

        form = CreatePasteForm(request.POST)

        if form.is_valid():

            if request.user.is_authenticated:               
                author = User.objects.get(username=request.user.username)                
                f = form.save(commit=False)
                f.author = author   
                created_paste = form.save()                
                return HttpResponseRedirect(reverse('paste:pasteView',kwargs={'id':int(created_paste.id)}))

            else:
                new_paste = form.save()
                return HttpResponseRedirect(reverse('paste:pasteView',kwargs={'id':int(new_paste.id)}))

    form = CreatePasteForm()
    return render(request, 'paste/create_paste.html', {'form': form})


def pasteView(request, id):
    # This view shows a particular paste which is passed on to the views
    latest_paste = Paste.objects.order_by('-created_at')[:5]
    paste = get_object_or_404(Paste, pk=id)    
    return render(request, 'paste/view_paste.html',{'paste':paste,'latest_paste':latest_paste})


#This view is called when the user is authenticated and wants to edit a post
def editPaste(request, id):
    paste = get_object_or_404(Paste, pk=id)
    
    if request.method == "POST":
        #Authenticated user edits his own paste
        if request.POST.get("edit-paste"):
            print('works')    
            form = EditPasteForm(request.POST,instance=paste)  
                
            if form.is_valid():
                print('working!')
                paste.edited = True    
                form.save()
                return paste.get_absolute_url()

        #Authenticated user edits someone else's paste
        else:
            form = CreatePasteForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.author = request.user
                new_paste = form.save()
                return new_paste.get_absolute_url()
    
    else:
        users_paste = Paste.objects.filter(author = request.user.id)
        if paste in users_paste:
            form = EditPasteForm(instance=paste)
            return render(request, 'paste/edit_paste.html', {'form': form})

        else:
            form = CreatePasteForm(instance=paste)
            return render(request, 'paste/create_paste.html', {'form': form})


def editPasteByGuest(request, id):
    # This view is called when a guest user tries to edit a paste 
    paste = get_object_or_404(Paste, pk=id)

    if request.method == "POST":

        form = CreatePasteForm(request.POST)  
                
        if form.is_valid():
            #print('working!')   
            new_paste = form.save()
            return new_paste.get_absolute_url()

    form = CreatePasteForm(instance=paste)
    return render(request, 'paste/create_paste.html', {'form': form})        
    

    


def pasteList(request):
    #This view renders a list of all the pastes
    pastes = Paste.objects.all().order_by('-created_at')
    ctx = {}
    ctx['header'] = ['Author','Title','Date']
    ctx['pastes'] = pastes
    
    return render(request, 'paste/list_of_pastes.html', ctx)    

def deletePaste(request, id):    
    paste = get_object_or_404(Paste, pk=id)
    paste.delete()
    return redirect('paste:pasteList')
