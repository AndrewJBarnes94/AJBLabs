import specialists

def chat(api_key, prompt):
    """
    Interact with the ChatGPT model and fetch its response based on the provided prompt.
    
    Args:
        api_key (str): OpenAI API key to authenticate the request.
        prompt (str): The question or message for the ChatGPT model.
    
    Returns:
        str: The response from the ChatGPT model.
    """
    API_KEY = api_key  # Set API Key
    chatbot = specialists.ChatGPT(API_KEY)  # Initialize the ChatGPT instance
    
    # Get a structured query from the provided prompt (can enhance for preprocessing in future)
    query = chatbot.get_prompt(prompt)
    
    # Fetch the response from ChatGPT based on the structured query
    response = chatbot.fetch_response(query)

    return response
