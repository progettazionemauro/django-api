import os

def run_script1():
    # Get the directory containing the current script file
    current_dir = os.path.dirname(__file__)
    # Construct the full path to the script
    script_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'progetto_api', 'add_page.sh'))
    return script_path


# Print the output directly in the terminal
print(run_script1())
