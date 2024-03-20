from django.urls import path
from .views import chatPage  # Import your view(s) here

urlpatterns = [
    path('chat/', chatPage, name='chat_page'),
    # Add more URL patterns if needed
]
