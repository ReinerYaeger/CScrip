from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process-prompt/',  csrf_exempt(views.process_prompt), name='process_prompt'),
    path('compile/', csrf_exempt(views.compile),name='compile')
]
