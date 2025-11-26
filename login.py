import tkinter.messagebox as messagebox
import tkinter as tk
import pandas as pd
import csv
import os

window = tk.Tk()
window.title("Login/Reg")
window.geometry("500x500")

user = ""
pas = ""

def get_info():
    global user, pas
    user = user_entry.get().strip()
    pas = pass_entry.get().strip()
    if user=="" or pas=="":
        messagebox.showerror("Error", "Fill Information")
        return False
    return True

def login_function():
    if not get_info(): return
    
    dt = pd.read_csv("dulieu.csv")

    if (((dt["username"]==user).value_counts().shape[0]) == 1):
        messagebox.showerror("Error", "Can not find Username")
    elif (((dt["username"]==user).value_counts().shape[0]) != 1) and (((dt["passw"]==pas).value_counts().shape[0]) == 1):
        messagebox.showerror("Error", "Wrong Password!")
    else:
        messagebox.showinfo("Information", "Login Successfully!")

def reg_function():
    if not get_info(): return
    dt = pd.read_csv("dulieu.csv")
    if (((dt["username"]==user).value_counts().shape[0]) == 1):
        with open("dulieu.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([user, pas])
        messagebox.showinfo("Information", "Reg Successfully!")
    else:
        messagebox.showerror("Error", "Exist Username!")

tk.Label(window, text='username', font=('Arial', 15)).grid(row=0, column=0, padx=20)
user_entry = tk.Entry(window, font=('Arial', 15))
user_entry.grid(row=0, column=1)

tk.Label(window, text='password', font=('Arial', 15)).grid(row=1, column=0, padx=20, pady=20)
pass_entry = tk.Entry(window, font=('Arial', 15))
pass_entry.grid(row=1, column=1, pady=20)

login_button = tk.Button(window, text="Login", font=('Arial', 15), command=login_function)
login_button.grid(row=2, column=1, padx=(0,100))

reg_button = tk.Button(window, text="Reg", font=('Arial', 15), command=reg_function)
reg_button.grid(row=2, column=2, padx=10)

window.mainloop()