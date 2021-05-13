from django.urls import path
from . import views
app_name = 'paste'

urlpatterns = [
    path('createpaste/', views.createPaste, name='createPaste'),
    path('pasteview/<int:id>',views.pasteView, name='pasteView'),
    path('editpaste/<int:id>', views.editPaste, name="editPaste"),
    path('deletepaste/<int:id>', views.deletePaste, name="deletePaste"),
    path('list-of-paste/',views.pasteList,name='pasteList')

]
    