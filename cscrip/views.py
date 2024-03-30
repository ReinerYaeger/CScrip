# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from chatgpt.chatgpt import cscrip_chatgpt


# Create your views here.

def index(request):
    context = {

    }
    return render(request, "index.html", context)


def process_prompt(request):
    if request.method == 'POST':
        prompt_text = request.POST.get('prompt', '')
        # Process prompt_text using chatgpt.py
        # Import and call functions from chatgpt.py as needed
        response_text = cscrip_chatgpt(prompt_text)
        return JsonResponse({'output': response_text})
    else:
        return JsonResponse({'error': 'Invalid request method'})
