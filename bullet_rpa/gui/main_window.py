import tkinter as tk
from tkinter import filedialog

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Bullet")
        self.root.geometry("300x700")

        # Robot name entry
        tk.Label(self.root, text="Robot Name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        # Robot path entry
        tk.Label(self.root, text="File Path:").pack()
        self.path_entry = tk.Entry(self.root)
        self.path_entry.pack()

        # File selection button
        file_button = tk.Button(self.root, text="Choose File", command=self.choose_file)
        file_button.pack()

        # Add robot button
        add_button = tk.Button(self.root, text="Add Robot", command=self.add_robot)
        add_button.pack()

        # List of robots
        self.robots = []

        # Listbox to display robots
        self.robot_listbox = tk.Listbox(self.root)
        self.robot_listbox.pack()

    def add_robot(self):
        robot_name = self.name_entry.get()
        robot_path = self.path_entry.get()
        robot = {"name": robot_name, "path": robot_path}
        self.robots.append(robot)
        print(f"Added Robot: {robot}")
        self.robot_listbox.insert(tk.END, f"{robot_name} ({robot_path})")

        # Clear entries
        self.name_entry.delete(0, tk.END)
        self.path_entry.delete(0, tk.END)

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, file_path)