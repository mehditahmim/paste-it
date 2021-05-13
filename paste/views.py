from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from django.urls.base import reverse
from .forms import CreatePasteForm,editPasteForm
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


def editPaste(request, id):
    paste = get_object_or_404(Paste, pk=id)
    if request.method == "POST":
        # print('works')
        form = editPasteForm(request.POST, instance=paste)
        print(form.errors)

        if form.is_valid():
            # print('working!')
            paste.edited = True
            form.save()
            return paste.get_absolute_url()

    form = editPasteForm(instance=paste)
    return render(request, 'paste/edit_paste.html', {'form': form})

def pasteList(request):
    #This view renders a list of all the pastes

    pastes = Paste.objects.all()
    ctx = {}
    ctx['header'] = ['Title', 'Text','Date']
    ctx['pastes'] = pastes
    
    return render(request, 'paste/list_of_pastes.html', ctx)    

def deletePaste(request, id):    
    paste = get_object_or_404(Paste, pk=id)
    paste.delete()
    return redirect('paste:pasteList')
