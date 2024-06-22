def run_script(self, request, queryset):
    # Get the directory containing the current script file
    current_dir = os.path.dirname(__file__)
    # Construct the full path to the script
    script_path = os.path.join(current_dir, '..', '..', 'progetto_api', 'add_page.sh')
    return script_path

# Print the output directly in the terminal
print(run_script(request, queryset))