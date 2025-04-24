import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Others": []
}

def organize_files(folder_path):
    # Create folders if not exist
    for folder in file_types:
        folder_name = os.path.join(folder_path, folder)
        os.makedirs(folder_name, exist_ok=True)

    # Move files to their respective folders
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        file_moved = False

        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                file_moved = True
                break

        if not file_moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", filename))

def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        organize_files(folder_path)
        messagebox.showinfo("Success", "Files organized successfully!")

# GUI setup
app = tk.Tk()
app.title("File Organizer")
app.geometry("300x150")
app.resizable(False, False)

label = tk.Label(app, text="Click the button to choose a folder to organize.")
label.pack(pady=20)

button = tk.Button(app, text="Choose Folder", command=choose_folder)
button.pack(pady=10)

app.mainloop()
