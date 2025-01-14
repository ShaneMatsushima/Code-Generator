import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from modules.template_render.template_render import streamlit_create

class ProjectSetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Setup")

        # Directory selection
        ttk.Label(root, text="Project Directory:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.directory_var = tk.StringVar()
        self.directory_entry = ttk.Entry(root, textvariable=self.directory_var, width=40)
        self.directory_entry.grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(root, text="Browse", command=self.browse_directory).grid(row=0, column=2, padx=10, pady=5)

        # Coding language selection
        ttk.Label(root, text="Coding Language:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.language_var = tk.StringVar()
        self.language_combo = ttk.Combobox(root, textvariable=self.language_var, state="readonly")
        self.language_combo['values'] = ("Python", "Java", "C", "C++")
        self.language_combo.grid(row=1, column=1, padx=10, pady=5)
        self.language_combo.bind("<<ComboboxSelected>>", self.update_options)

        # Placeholder for dynamic options
        self.extra_option_frame = ttk.Frame(root)
        self.extra_option_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="w")

        # Project name
        ttk.Label(root, text="Project Name:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.project_name_var = tk.StringVar()
        self.project_name_entry = ttk.Entry(root, textvariable=self.project_name_var, width=40)
        self.project_name_entry.grid(row=3, column=1, padx=10, pady=5)

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
                ttk.Label(self.extra_option_frame, text="Python Project Type:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
                self.python_project_type_var = tk.StringVar()
                python_project_type_combo = ttk.Combobox(self.extra_option_frame, textvariable=self.python_project_type_var, state="readonly")
                python_project_type_combo['values'] = ("Flask", "Streamlit", "Regular Python Project")
                python_project_type_combo.grid(row=0, column=1, padx=10, pady=5)
                python_project_type_combo.bind("<<ComboboxSelected>>", self.update_python_project_options)
            case "Java":
                pass
            case "C":
                pass
            case "C++":
                pass

    def update_python_project_options(self, event=None):
        selected_project_type = self.python_project_type_var.get()

        for widget in self.extra_option_frame.winfo_children():
            widget.destroy()

        match selected_project_type:
            case "Streamlit":
                # Streamlit-specific options
                ttk.Label(self.extra_option_frame, text="App Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
                self.app_name_var = tk.StringVar()
                ttk.Entry(self.extra_option_frame, textvariable=self.app_name_var, width=40).grid(row=0, column=1, padx=10, pady=5)

                ttk.Label(self.extra_option_frame, text="App Title:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
                self.app_title_var = tk.StringVar()
                ttk.Entry(self.extra_option_frame, textvariable=self.app_title_var, width=40).grid(row=1, column=1, padx=10, pady=5)

                ttk.Label(self.extra_option_frame, text="App Header:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
                self.app_header_var = tk.StringVar()
                ttk.Entry(self.extra_option_frame, textvariable=self.app_header_var, width=40).grid(row=2, column=1, padx=10, pady=5)

                ttk.Label(self.extra_option_frame, text="App Description:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
                self.app_description_var = tk.StringVar()
                ttk.Entry(self.extra_option_frame, textvariable=self.app_description_var, width=40).grid(row=3, column=1, padx=10, pady=5)

                ttk.Label(self.extra_option_frame, text="Sidebar Options (comma-separated):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
                self.sidebar_options_var = tk.StringVar()
                ttk.Entry(self.extra_option_frame, textvariable=self.sidebar_options_var, width=40).grid(row=4, column=1, padx=10, pady=5)

                ttk.Label(self.extra_option_frame, text="Show Chart:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
                self.show_chart_var = tk.BooleanVar()
                ttk.Checkbutton(self.extra_option_frame, variable=self.show_chart_var).grid(row=5, column=1, padx=10, pady=5)

                ttk.Label(self.extra_option_frame, text="Show Data:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
                self.show_data_var = tk.BooleanVar()
                ttk.Checkbutton(self.extra_option_frame, variable=self.show_data_var).grid(row=6, column=1, padx=10, pady=5)

            case "Flask":
                pass
            case "Regular Python Project":
                pass
        

    def create_project(self):
        directory = self.directory_var.get()
        language = self.language_var.get()
        project_name = self.project_name_var.get()

        if not directory or not language or not project_name:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        match language:
            case "Python":
                match self.python_project_type_var.get():
                    case "Streamlit":
                        app_name = self.app_name_var.get()
                        app_title = self.app_title_var.get()
                        app_header = self.app_header_var.get()
                        app_description = self.app_description_var.get()
                        sidebar_options = self.sidebar_options_var.get().split(",")
                        show_chart = self.show_chart_var.get()
                        show_data = self.show_data_var.get()

                        #create streamlit file for project
                        streamlit_create(directory, app_name, app_title, app_header,
                                         app_description, sidebar_options, show_chart, show_data)

                        # Handle Streamlit project creation (placeholder logic)
                        messagebox.showinfo(
                            "Streamlit Project",
                            f"Streamlit app '{app_name}' created with the following options:\n"
                            f"Title: {app_title}\nHeader: {app_header}\nDescription: {app_description}\n"
                            f"Sidebar Options: {sidebar_options}\nShow Chart: {show_chart}\nShow Data: {show_data}"
                        )

                        

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSetupApp(root)
    root.mainloop()
