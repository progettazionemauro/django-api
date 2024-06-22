from django.http import HttpResponse

def run_script_view(request):
    # Import your script here (replace 'your_script' with the actual script name)
    from . import your_script

    # Call the script function and handle any output/errors
    try:
        result = your_script.run_script()
        message = f"Script execution successful! Output: {result}"
    except Exception as e:
        message = f"Script execution failed: {str(e)}"

    return HttpResponse(message)
