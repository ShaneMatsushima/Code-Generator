from jinja2 import Template
import os

# ========= Python Project Versions ============
STREAMLIT_VERSION = "streamlit==1.41.1"
FLASK_VERSION = "Flask==3.1.0"
# ==============================================

"""
    Creates a Streamlit app file in the specified directory based on user inputs.
    Creates requirements.txt file for project.
    Creates run_app script for project.

    Parameters:
        dir (str): Directory where the app file should be created.
        app_name (str): Name of the app (used as the filename).
        app_title (str): Title of the app.
        app_header (str): Header for the app.
        app_desc (str): Description of the app.
        sidebar_options (list): List of sidebar options.
        show_chart (bool): Whether to include a chart in the app.
        show_data (bool): Whether to include a data table in the app.
"""
def streamlit_create(dir:str, app_name:str, app_title:str, app_header:str, app_desc:str, 
                     sidebar_options:list, show_chart=False, show_data=False):
    # Ensure the directory exists
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Construct the template file path two directories above the current script
    script_dir = os.path.dirname(__file__)
    template_path = os.path.join(script_dir, "..", "..", "templates", "streamlit_template.template")
    template_path = os.path.abspath(template_path)

    # Read the template file
    try:
        with open(template_path, "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file not found at: {template_path}")

    template = Template(template_content)

    # Render the template with user inputs
    rendered_content = template.render(
        app_name=app_name,
        app_title=app_title,
        app_header=app_header,
        app_description=app_desc,
        sidebar_options=sidebar_options,
        show_chart=show_chart,
        show_data=show_data
    )

    # Create Streamlit Main File
    file_name = f"{app_name.lower().replace(' ', '_')}.py"
    app_path = os.path.join(dir, file_name)
    with open(app_path, "w") as file:
        file.write(rendered_content)

    print(f"Streamlit app '{file_name}' created successfully")

    # Create python requirements file
    requ_file = "requirements.txt"
    requ_path = os.path.join(dir, requ_file)
    with open(requ_path, "w") as file:
        file.write(STREAMLIT_VERSION)
    
    print(f"Requirements.txt created succcessfully")

   # Create Batch or Shell script to run the Streamlit app

    STREAMLIT_BATCH = f"""@echo off
    cd /d "{dir}"
    REM Starting Streamlit App
    streamlit run {file_name}
    echo Starting Streamlit App
    """

    STREAMLIT_SHELL = f"""#!/bin/bash
    cd "{dir}" || exit
    # Starting Streamlit App
    streamlit run {file_name}
    """

    # Determine file type based on OS
    script_file = "run_app.bat" if os.name == "nt" else "run_app.sh"
    script_path = os.path.join(dir, script_file)

    # Choose the correct script content based on OS
    os_write = STREAMLIT_BATCH if os.name == "nt" else STREAMLIT_SHELL

    # Write the script to the file
    with open(script_path, "w") as script_file:
        script_file.write(os_write)

    # If shell script, make it executable
    if os.name != "nt":
        os.chmod(batch_path, 0o755)

    print(f"Run App Script created successfully")

"""
    Creates a Flask app file in the specified directory based on user inputs.
    Creates requirements.txt file for project.
    Creates run_app script for project.

    Parameters:
        dir (str): Directory where the app file should be created.
        endpoint_count (int): number of endpoints for the project to create
"""
def flask_create(dir:str, endpoint_count:int):
    # Ensure the directory exists
    if not os.path.exists(dir):
        os.makedirs(dir)

    file_str = 'from flask import Flask, jsonify, request \n \n'

    file_str += 'app = Flask(__name__)'

    if endpoint_count is not None:
        for endpoint in range(endpoint_count):
            file_str += f'\n@app.route("//", methods=["GET", "POST"]) '
            file_str += f'\ndef name{endpoint}():\n \t pass \n' 
    else:
        file_str += '\n@app.route("/", methods=["GET", "POST"]) \n'
        file_str += 'def home(): \n \t pass \n'

    file_str += '\n \n'
    file_str += "if __name__ == '__main__': \n"
    file_str += '\tapp.run(debug=True)'

    # Create Flask main file
    file_dir = os.path.join(dir, "api.py")
    with open(file_dir, "w") as file:
        file.write(file_str)
        print(f"Flask App created successfully in {dir}")

    # Create requirements.txt
    requ_file = "requirements.txt"
    requ_path = os.path.join(dir, requ_file)
    with open(requ_path, "w") as file:
        file.write(FLASK_VERSION)
    
    print(f"Requirements.txt created succcessfully")

    # Create Batch or Shell script to run flask api
    FLASK_BATCH = f"""@echo off
    cd {dir}
    echo -------------
    echo Running API Server .....
    echo -------------
    :: run flask API
    flask --app api run 
    """

    FLASK_SHELL = f"""#!/bin/bash
    echo -------------
    echo Running API Server .....
    echo -------------
    # run flask API
    flask --app api run
    """
    
    # Determine file type based on OS
    script_file = "run_app.bat" if os.name == "nt" else "run_app.sh"
    script_path = os.path.join(dir, script_file)

    # Choose the correct script content based on OS
    os_write = FLASK_BATCH if os.name == "nt" else FLASK_SHELL

    # Write the script to the file
    with open(script_path, "w") as script_file:
        script_file.write(os_write)

    # If shell script, make it executable
    if os.name != "nt":
        os.chmod(batch_path, 0o755)
    
    print(f"Run App Script created successfully")


"""
    Creates a python file in the specified directory based on user inputs.
    Creates requirements.txt file for project.
    Creates run_app script for project.

    Parameters:
        dir (str): Directory where the app file should be created.
        proj_name (str): Name of file or project to create
"""
def regular_python_create(dir:str, proj_name:str):
    # Ensure the directory exists
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    file_str = "\n \n \nif __name__ == '__main__': \n \tpass"

    # Create Python main file
    file_name = f"{proj_name.lower().replace(' ', '_')}.py"
    file_dir = os.path.join(dir, file_name)
    with open(file_dir, "w") as file:
        file.write(file_str)
        print(f"Python script created successfully in {dir}")
    
    # Create requirements.txt
    requ_file = "requirements.txt"
    requ_path = os.path.join(dir, requ_file)
    with open(requ_path, "w") as file:
        file.write('# Place requirements here')
    
    print(f"Requirements.txt created succcessfully")

    PYTHON_BATCH = f"""@echo off
    cd {dir}
    echo -------------
    echo Running Python Script .....
    echo -------------
    python {file_name}
    """

    PYTHON_SHELL = f"""#!/bin/bash
    echo -------------
    echo Running Python Script .....
    echo -------------
    python {file_name}
    """

    # Determine file type based on OS
    script_file = "run_app.bat" if os.name == "nt" else "run_app.sh"
    script_path = os.path.join(dir, script_file)

    # Choose the correct script content based on OS
    os_write = PYTHON_BATCH if os.name == "nt" else PYTHON_SHELL

    # Write the script to the file
    with open(script_path, "w") as script_file:
        script_file.write(os_write)

    # If shell script, make it executable
    if os.name != "nt":
        os.chmod(batch_path, 0o755)
    
    print(f"Run App Script created successfully")


    


    


    

        



