from jinja2 import Template
import os
import shutil

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

"""
    Creates a Java project in the specified directory based on user inputs.
    Creates README.md file for project.
    Creates pom.xml for project.

    Parameters:
        dir (str): Directory where the app file should be created.
        proj_name (str): Name of file or project to create
        test (bool): Flag for unti testing creation
"""
def java_create(dir:str, proj_name:str, test_flag:bool):

    # == Init Project Creation ==

    # restructure proj_name
    proj_name = proj_name.lower().replace(' ', '_')

    # create paths for files
    com_path = "src/main/java/com"

    main_file_path = com_path + f"/{proj_name}"
    dir_path = os.path.join(dir, main_file_path)
    os.makedirs(dir_path, exist_ok=True)

    utils_path = com_path + "/utils"
    dir_path = os.path.join(dir, utils_path)
    os.makedirs(dir_path, exist_ok=True)

    service_path = com_path + "/services"
    dir_path = os.path.join(dir, service_path)
    os.makedirs(dir_path, exist_ok=True)

    # string to place in file

    # -- MAIN --
    main_str = "package com.example;\n\n"
    main_str += "import com.example.services.CalculatorService;\n\n"
    main_str += "public class Main {\n"
    main_str += "\tpublic static void main(String[] args) {\n"
    main_str += "\t\tSystem.out.println(\"Welcome to the Java Starter Project\");"
    main_str += "\t\tCalculatorService calculator = new CalculatorService();\n"
    main_str += "\t\tint sum = calculator.add(5,10);\n"
    main_str += "\t\tSystem.out.println(\"Sum: \" + sum);\n"
    main_str += "\t}\n"
    main_str += "}\n"

    # -- StringUtils.java --
    utils_str = "package com.example.utils;\n\n"
    utils_str += "public class StringUtils {\n"
    utils_str += "\tpublic static boolean isEmpty(String str) {\n"
    utils_str += "\t\treturn str == null || str.isEmpty();\n"
    utils_str += "\t}\n"
    utils_str += "}\n"

    # -- CalculatorService.java --
    calc_serv_str = "package com.example.services;\n\n"
    calc_serv_str += "public class CalculatorService {\n"
    calc_serv_str += "\tpublic int add(int a, int b) {\n"
    calc_serv_str += "\t\treturn a + b;\n"
    calc_serv_str += "\t}\n"
    calc_serv_str += "}\n"

    # file creation and writing
    #create main file
    main_path = os.path.join(dir, main_file_path)
    main_path = os.path.join(main_path, f"{proj_name}.java")
    with open(main_path, "w") as file:
        file.write(main_str)

    utils_path = os.path.join(dir, utils_path)
    utils_path = os.path.join(utils_path, "StringUtils.java")
    with open(utils_path, "w") as file:
        file.write(utils_str)
    
    service_path = os.path.join(dir, service_path)
    service_path = os.path.join(service_path, "CalculatorService.java")
    with open(service_path, "w") as file:
        file.write(calc_serv_str)

    # pom.xml creation
    pom_path = os.path.join(dir, "pom.xml")
    script_dir = os.path.dirname(__file__)
    template_path = os.path.join(script_dir, "..", "..", "templates", "pom.template")
    template_path = os.path.abspath(template_path)
    copy_template(template_path, pom_path)

    # Create ReadMe file
    readme_path = os.path.join(dir, "README.md")
    template_path = os.path.join(script_dir, "..", "..", "templates", "javaReadMe.template")
    template_path = os.path.abspath(template_path)
    copy_template(template_path, readme_path)

    # == Test Unit Creation ==
    if test_flag:
        test_path = "test/java/com/" + f"{proj_name}"
        test_dir_path = os.path.join(dir, test_path)

        # -- Main Test --
        main_test_str = "package com.example;\n\n"
        main_test_str += "import org.junit.jupiter.api.Test;\n"
        main_test_str += "import static org.junit.jupiter.api.Assertions.*;\n\n"
        main_test_str += "public class MainTest {\n"
        main_test_str += "\t@Test\n"
        main_test_str += "\tpublic void testMain() {\n"
        main_test_str += "\t\tassertTrue(true)\n;"
        main_test_str += "\t}\n"
        main_test_str += "}\n"

        # -- Calculator Test --
        calc_test_str = "package com.example.services;\n\n"
        calc_test_str += "import org.junit.jupiter.api.Test;\n"
        calc_test_str += "import static org.junit.jupiter.api.Assertions.*;\n\n"
        calc_test_str += "public class CalculatorServiceTest {\n"
        calc_test_str += "\t@Test\n"
        calc_test_str += "\tpublic void testAdd() {\n"
        calc_test_str += "\t\tCalculatorService calculator = new CalculatorService();"
        calc_test_str += "\t\tassertEquals(15, calculator.add(10,5));"
        calc_test_str += "\t}\n"
        calc_test_str += "}\n"



        os.makedirs(test_dir_path, exist_ok=True)
        main_test_path = os.path.join(test_dir_path, f"{proj_name}Test.java")
        with open(main_test_path, "w") as file:
            file.write(main_test_str)

        test_service_path = os.path.join(test_dir_path, "services")
        os.makedirs(test_service_path, exist_ok=True)
        calc_test_path = os.path.join(test_service_path, "CalculatorServiceTest.java")
        with open(calc_test_path, "w") as file:
            file.write(calc_test_str)

#TODO
def java_frc_sim_create(dir:str, name:str):
    pass

#TODO
def java_frc_create(dir:str, name:str):
    pass


"""
    Helper function to copy and paste template content into new file

    Parameters:
    template_path (str): Path to the template file
    output_path (str): Path to the output file
"""
def copy_template(template_path, new_file_path):
    try:
        shutil.copy(template_path, new_file_path)
    except FileNotFoundError:
        print(f"Template file {template_path} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    






    


    


    

        



