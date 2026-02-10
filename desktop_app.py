import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/api/upload/"

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        with open(file_path, "rb") as f:
            response = requests.post(API_URL, files={"file": f}, timeout=10)

        print("Status:", response.status_code)
        print("Response:", response.text)

        if response.status_code != 200:
            messagebox.showerror("Server Error", response.text)
            return

        data = response.json()
        show_chart(data)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_chart(data):
    labels = list(data["type_distribution"].keys())
    values = list(data["type_distribution"].values())

    plt.bar(labels, values)
    plt.title("Equipment Distribution")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.show()

root = tk.Tk()
root.title("Chemical Visualiser Desktop")

btn = tk.Button(root, text="Upload CSV", command=upload_file)
btn.pack(padx=40, pady=40)

root.mainloop()
