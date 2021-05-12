from django.urls import path
from . import views
app_name = 'paste'

urlpatterns = [
    path('createpaste/', views.createPaste, name='createPaste'),
    path('pasteview/<int:id>',views.pasteView, name='pasteView')

]
    