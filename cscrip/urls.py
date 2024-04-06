from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process-prompt/', views.process_prompt, name='process_prompt'),
    path('compile/',views.compile,name='compile')
]
