from jinja2 import Template

def streamlit_create(app_name:str, ):
    # Create a Jinja2 template
    with open("..\\templates\\streamlit_template.py", "r") as file:
        template_content = file.read()

    template = Template(template_content)

    template_values = {
        "app_name" : app_name,
        "app_title" : app_name.capitalize(),
        "app_header" : app_name,

    }