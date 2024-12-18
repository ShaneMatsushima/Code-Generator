import tkinter as tk
from tkinter import ttk, filedialog, messagebox

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

        # Project type selection
        ttk.Label(root, text="Project Type:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.project_type_var = tk.StringVar()
        self.project_type_combo = ttk.Combobox(root, textvariable=self.project_type_var, state="readonly")
        self.project_type_combo['values'] = ("Streamlit", "FRC Robot", "FTC Robot", "Tkinter GUI")
        self.project_type_combo.grid(row=2, column=1, padx=10, pady=5)

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

    def create_project(self):
        directory = self.directory_var.get()
        language = self.language_var.get()
        project_type = self.project_type_var.get()
        project_name = self.project_name_var.get()

        if not all([directory, language, project_type, project_name]):
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        message = (
            f"Project Details:\n"
            f"Directory: {directory}\n"
            f"Language: {language}\n"
            f"Type: {project_type}\n"
            f"Name: {project_name}"
        )
        messagebox.showinfo("Project Created", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSetupApp(root)
    root.mainloop()