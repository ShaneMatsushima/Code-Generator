import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from modules.template_render.template_render import streamlit_create, flask_create, regular_python_create, java_create, java_frc_sim_create

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
        match selected_language:
            case "Python":
                self.create_python_options()
            
            case "C":
                self.create_c_options()
            
            case "C++":
                self.create_cpp_options()
            
            case "Java":
                self.create_java_options()

    def create_python_options(self):
        ttk.Label(self.extra_option_frame, text="Python Project Type:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.python_project_type_var = tk.StringVar()
        python_project_type_combo = ttk.Combobox(
            self.extra_option_frame, textvariable=self.python_project_type_var, state="readonly"
        )
        python_project_type_combo['values'] = ("Flask", "Streamlit", "Regular Python Project")
        python_project_type_combo.grid(row=0, column=1, padx=10, pady=5)
        python_project_type_combo.bind("<<ComboboxSelected>>", self.update_python_project_options)

    def create_java_options(self):
        ttk.Label(self.extra_option_frame, text="Java Project Type:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.java_project_type_var = tk.StringVar()
        java_project_type_combo = ttk.Combobox(
            self.extra_option_frame, textvariable=self.java_project_type_var, state="readonly"
            )
        java_project_type_combo['values'] = ("FRC Sim", "Java Reg", "FRC Reg")
        java_project_type_combo.grid(row=0, column=1, padx=10, pady=5)
        java_project_type_combo.bind("<<ComboboxSelected>>", self.update_java_project_options)

    #TODO
    def create_c_options(self):
        ...

    #TODO
    def create_cpp_options(self):
        ...

    def create_java_frc_options(self):
        ...
    
    def create_java_frc_sim_options(self):
        self.sim_sub_name = tk.StringVar()
        ttk.Label(self.extra_option_frame, text="Sim Name:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Entry(self.extra_option_frame, textvariable=self.sim_sub_name).grid(row=0, column=1, padx=10, pady=5)

        self.sim_sub_type = tk.StringVar()
        ttk.Label(self.extra_option_frame, text="Type of Subsystem:").grid(row=1, column=0, padx=10, pady=5)
        sim_sub_combo = ttk.Combobox(self.extra_option_frame, textvariable=self.sim_sub_type, state="readonly")
        sim_sub_combo['values'] = ("Roller", "Elevator")
        sim_sub_combo.grid(row=1, column=1, padx=10, pady=5)

        self.sim_motor_type = tk.StringVar()
        ttk.Label(self.extra_option_frame, text="Motor Type:").grid(row=2, column=0, padx=10, pady=5)
        sim_motor_combo = ttk.Combobox(self.extra_option_frame, textvariable=self.sim_motor_type, state="readonly")
        sim_motor_combo['values'] = ("TalonFX", "SparkMax")
        sim_motor_combo.grid(row=2, column=1, padx=10, pady=5)

        self.sim_can_id = tk.IntVar()
        ttk.Label(self.extra_option_frame, text="Can ID").grid(row=3, column=0, padx=10, pady=5)
        ttk.Entry(self.extra_option_frame, textvariable=self.sim_can_id).grid(row=3,column=1, padx=10, pady=5)

        self.sim_current_limit = tk.IntVar()
        ttk.Label(self.extra_option_frame, text="Current Limit").grid(row=4, column=0, padx=10, pady=5)
        ttk.Entry(self.extra_option_frame, textvariable=self.sim_current_limit).grid(row=4,column=1, padx=10, pady=5)

        self.sim_motor_reduction = tk.DoubleVar()
        ttk.Label(self.extra_option_frame, text="Motor Reduction").grid(row=5, column=0, padx=10, pady=5)
        ttk.Entry(self.extra_option_frame, textvariable=self.sim_motor_reduction).grid(row=5, column=1, padx=10, pady=5)



    def create_java_reg_options(self):
        self.java_project_test = tk.BooleanVar()
        ttk.Checkbutton(self.extra_option_frame, text="Unit Tests", variable=self.java_project_test).grid(row=1, column=0, padx=10, pady=5, sticky="w")

    def update_java_project_options(self, event=None):
        for widget in self.extra_option_frame.winfo_children():
            widget.destroy()

        selected_project_type = self.java_project_type_var.get()
        match selected_project_type:
            case "FRC Sim":
                self.create_java_frc_sim_options()
            case "FRC Reg":
                self.create_java_frc_options()
            case "Java Reg":
                self.create_java_reg_options()

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
        
        if language == "Python" and self.python_project_type_var.get() == "Regular Python Project":
            # Create regular Python project
            regular_python_create(directory, project_name)
            messagebox.showinfo("Success", f"Regular Python project '{project_name}' created successfully!")

        if language == "Java" and self.java_project_type_var == "Java Reg":
            # Create Java project
            java_create(directory, project_name, self.java_project_test)
            messagebox.showinfo("Success", f"Java project '{project_name}' created successfully!")

        if language == "Java" and self.java_project_type_var.get() == "FRC Sim":

            print("Generating FRC Sim Code")

            success_message = f"Successfully generated sim code for {project_name}\nPlease Note: The generated folder with code should be dropped into the subsystem directory in FRC code."

            sub_name = self.sim_sub_name.get()
            sub_type = self.sim_sub_type.get()
            sim_motor_type = self.sim_motor_type.get()
            sim_can_id = self.sim_can_id.get()
            sim_current_limit = self.sim_current_limit.get()
            sim_motor_reduction = self.sim_motor_reduction.get()


            # Create FRC Sim project
            java_frc_sim_create(directory, sub_name, sub_type, sim_motor_type, sim_can_id, sim_current_limit, sim_motor_reduction)
            messagebox.showinfo("Success", success_message)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSetupApp(root)
    root.mainloop()