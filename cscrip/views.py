# Create your views here.
import json
from django.shortcuts import render
from django.http import JsonResponse
from httpcore import Response
from .cscrip_complier import compiler
import cscrip
from chatgpt.chatgpt import custom_chat


# Create your views here.

def index(request):
    context = {

    }
    return render(request, "index.html", context)


async def compile(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        content = compiler(code)
        # content = content.strip('\n', ' ')

        if isinstance(content, Response):
            program = content.text
            serialized_data = json.dumps({program})
            return JsonResponse({'output': serialized_data}, safe=False)
        else:
            return JsonResponse({'output': str(content)})
    return JsonResponse({'error': 'Invalid request method'})


async def process_prompt(request):
    if request.method == 'POST':
        prompt_text = request.POST.get('prompt', '')
        response_text = custom_chat(prompt_text)
        # Check if response_text is a Response object
        if isinstance(response_text, Response):
            # Handle the Response object accordingly
            # For example, extract the content
            content = response_text.text  # Assuming the content can be accessed via a text attribute

            # Construct serialized data dictionary
            serialized_data = {'content': content}

            # Return JsonResponse with serialized data
            return JsonResponse({'output': serialized_data})
        else:
            # If response_text is not a Response object, handle it accordingly
            return JsonResponse({'output': str(response_text)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
