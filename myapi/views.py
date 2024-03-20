from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def chatPage(request):
    # Assuming you want to render a template named 'chatPage.html'
    return render(request, 'chatPage.jsx')