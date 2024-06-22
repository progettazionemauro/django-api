from django.http import HttpResponse

def run_script_view(request):
    # Simpler script (prints a message)
    message = "This is a test script!"

    # Handle script execution (no external script in this example)
    try:
        # Simulate script execution
        print(message)
        result = "Script executed successfully."
    except Exception as e:  # This wouldn't be triggered in this example
        result = f"Script execution failed: {str(e)}"

    return HttpResponse(result)
