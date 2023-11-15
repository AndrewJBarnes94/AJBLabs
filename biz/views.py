from django.shortcuts import render
from . import specialists
from .models import Davinci002_Query_Log, ProjectManagerAssistant

def biz_home(request):
    return render(request, 'biz_home.html', {})

def genaius(request):

    if request.method == 'POST':
        prompt_input = request.POST.get('prompt_input', '')
        pre_prompt = 'Make me a list of 5 things, serialized in JSON (where keys are identification numbers and values are list items), that pertain to this prompt if it makes sense:\n "'
        post_prompt = '" If the prompt makes absolutely zero sense (not english, jibberish, etc), respond with "INVALID PROMPT". Include both curly brackets for proper JSON and do not respond with anything but the JSON if the prompt is valid.'
        prompt = pre_prompt + prompt_input + post_prompt

        API_KEY = "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"  # Set API Key
        chatbot = specialists.ChatGPT(API_KEY)  # Initialize the ChatGPT instance
        
        # Get a structured query from the provided prompt (can enhance for preprocessing in future)
        query = chatbot.get_prompt(prompt)
        
        # Fetch the response from ChatGPT based on the structured query
        response = chatbot.fetch_response(query)

        # Save to Davinci002_Query_Log
        log_entry = Davinci002_Query_Log(
            pre_prompt=pre_prompt,
            prompt=prompt_input,
            post_prompt=post_prompt,
            response=response,
        )
        log_entry.save()

        return render(
            request,
            'genaius.html', 
            {
                "prompt_input": prompt_input,
                "pre_prompt": pre_prompt,
                "post_prompt": post_prompt,
                "prompt": prompt,
                "response": response,
            }
        )
    return render(request, 'genaius.html', {})

def biz_logs(request):
    all_records = Davinci002_Query_Log.objects.all()
    return render(request, 'biz_logs.html', {'records': all_records, 'count': 0})

def proj_management(request):
    if request.method == 'POST':
        prompt_input = request.POST.get('prompt_input', '')
        pre_prompt = 'Given the project task, generate a list of actionable items: "'
        post_prompt = '" Provide the list in a simple bullet point format using five bullets max.'
        prompt = pre_prompt + prompt_input + post_prompt

        API_KEY = "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"  # Set API Key
        chatbot = specialists.ChatGPT(API_KEY)  # Initialize the ChatGPT instance
        
        # Get a structured query from the provided prompt (can enhance for preprocessing in future)
        query = chatbot.get_prompt(prompt)
        
        # Fetch the response from ChatGPT based on the structured query
        response = chatbot.fetch_response(query)
        bullet_points = response.split('\n')
        bullet_points = [point.lstrip('• ').rstrip() for point in bullet_points if point.strip() != '']
        print(response)
        # Save to Davinci002_Query_Log
        log_entry = ProjectManagerAssistant(
            pre_prompt=pre_prompt,
            prompt=prompt_input,
            post_prompt=post_prompt,
            response=response,
        )
        log_entry.save()

        return render(
            request,
            'proj_management.html', 
            {
                "prompt_input": prompt_input,
                "pre_prompt": pre_prompt,
                "post_prompt": post_prompt,
                "prompt": prompt,
                "response": response,
                "bullet_points": bullet_points,
            }
        )
    return render(request, 'proj_management.html', {})