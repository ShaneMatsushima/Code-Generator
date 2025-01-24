import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from modules.template_render.template_render import streamlit_create, flask_create

class ProjectSetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Setup")

        # Directory selection
        ttk.Label(root, text="Project Directory:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.directory_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.directory_var, width=40).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(root, text="Browse", command=self.browse_directory).grid(row=0, column=2, padx=10, pady=5)

        # Coding language selection
        ttk.Label(root, text="Coding Language:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.language_var = tk.StringVar()
        self.language_combo = ttk.Combobox(root, textvariable=self.language_var, state="readonly")
        self.language_combo['values'] = ("Python", "Java", "C", "C++")
        self.language_combo.grid(row=1, column=1, padx=10, pady=5)
        self.language_combo.bind("<<ComboboxSelected>>", self.update_options)

        # Dynamic options frame
        self.extra_option_frame = ttk.Frame(root)
        self.extra_option_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="w")

        # Project name
        ttk.Label(root, text="Project Name:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.project_name_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.project_name_var, width=40).grid(row=3, column=1, padx=10, pady=5)

        # Submit button
        ttk.Button(root, text="Create Project", command=self.create_project).grid(row=4, column=0, columnspan=3, pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_var.set(directory)

    def update_options(self, event=None):
        # Clear existing options
        for widget in self.extra_option_frame.winfo_children():
            widget.destroy()

        selected_language = self.language_var.get()
        if selected_language == "Python":
            self.create_python_options()
        # Additional languages can be handled here (Java, C, etc.)

    def create_python_options(self):
        ttk.Label(self.extra_option_frame, text="Python Project Type:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.python_project_type_var = tk.StringVar()
        python_project_type_combo = ttk.Combobox(
            self.extra_option_frame, textvariable=self.python_project_type_var, state="readonly"
        )
        python_project_type_combo['values'] = ("Flask", "Streamlit", "Regular Python Project")
        python_project_type_combo.grid(row=0, column=1, padx=10, pady=5)
        python_project_type_combo.bind("<<ComboboxSelected>>", self.update_python_project_options)

    def update_python_project_options(self, event=None):
        # Clear dynamic options
        for widget in self.extra_option_frame.winfo_children():
            widget.destroy()

        selected_project_type = self.python_project_type_var.get()
        if selected_project_type == "Streamlit":
            self.create_streamlit_options()
        elif selected_project_type == "Flask":
            self.create_flask_options()

    def create_streamlit_options(self):
        options = [
            ("App Name", "app_name_var"),
            ("App Title", "app_title_var"),
            ("App Header", "app_header_var"),
            ("App Description", "app_description_var"),
            ("Sidebar Options (comma-separated)", "sidebar_options_var"),
        ]

        for i, (label, var_name) in enumerate(options):
            setattr(self, var_name, tk.StringVar())
            ttk.Label(self.extra_option_frame, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ttk.Entry(self.extra_option_frame, textvariable=getattr(self, var_name), width=40).grid(row=i, column=1, padx=10, pady=5)

        self.show_chart_var = tk.BooleanVar()
        ttk.Checkbutton(self.extra_option_frame, text="Show Chart", variable=self.show_chart_var).grid(row=len(options), column=0, columnspan=2, sticky="w")

        self.show_data_var = tk.BooleanVar()
        ttk.Checkbutton(self.extra_option_frame, text="Show Data", variable=self.show_data_var).grid(row=len(options) + 1, column=0, columnspan=2, sticky="w")

    def create_flask_options(self):
        ttk.Label(self.extra_option_frame, text="Endpoint Count:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.endpoint_count_var = tk.IntVar()
        ttk.Entry(self.extra_option_frame, textvariable=self.endpoint_count_var, width=10).grid(row=0, column=1, padx=10, pady=5)

    def create_project(self):
        directory = self.directory_var.get()
        language = self.language_var.get()
        project_name = self.project_name_var.get()

        if not directory or not language or not project_name:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        if language == "Python" and self.python_project_type_var.get() == "Streamlit":
            app_name = self.app_name_var.get()
            app_title = self.app_title_var.get()
            app_header = self.app_header_var.get()
            app_description = self.app_description_var.get()
            sidebar_options = self.sidebar_options_var.get().split(",")
            show_chart = self.show_chart_var.get()
            show_data = self.show_data_var.get()

            # Create Streamlit project
            streamlit_create(directory, app_name, app_title, app_header, app_description, sidebar_options, show_chart, show_data)
            messagebox.showinfo("Success", f"Streamlit project '{app_name}' created successfully!")

        if language == "Python" and self.python_project_type_var.get() == "Flask":
            endpoint_count = self.endpoint_count_var.get()
            if endpoint_count <= 0:
                messagebox.showerror("Error", "Please enter a valid endpoint count.")
                return
            
            # Create Flask project
            flask_create(directory, endpoint_count)
            messagebox.showinfo("Success", f"Flask API project '{project_name}' create successfully!")
        
        


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSetupApp(root)
    root.mainloop()