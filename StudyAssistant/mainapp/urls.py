'''
Contains URLs of mainapp.

Any new URL added to mainapp needs to be defined here as first argument
of path function. The corresponnding view function name for the url also
needs to mentioned as second argument of path function. The third argument
is the name provided to the url.
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('deadline', views.deadline, name='deadline'),
    path('notes', views.notes, name='notes'),
    path('add_deadline', views.add_deadline, name='add_deadline'),
    path('put_deadline', views.put_deadline,name='put_deadline'),
    path('delete_deadline', views.delete_deadline,name='delete_deadline'),
    path('add_note', views.add_note, name='add_note'),
    path('put_note', views.put_note,name='put_note'),
    path('view_note', views.view_note,name='view_note'),
    path('delete_note', views.delete_note,name='delete_note'),
]
