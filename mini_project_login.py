from asyncio import constants
from calendar import c
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
authcode = 666666

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
    user_data = dt[dt['username']==user]
    
    if (user_data.empty):
        messagebox.showerror("Error", "Can not find Username")
    else:
        if (user_data["passw"]==pas).any():
            messagebox.showinfo("Information", "Login Successfully")
        else:
            messagebox.showerror("Error", "Wrong Password")


def reg_function():
    global authcode
    if not get_info(): return
    dt = pd.read_csv("dulieu.csv")
    authcode = facode_entry.get().strip()
    user_data = dt[dt['username']==user]

    if authcode == "":
        authcode = 666666

    if (user_data.empty):
        with open("dulieu.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([user, pas, authcode])
        messagebox.showinfo("Information", "Reg Successfully!")
    else:
        messagebox.showerror("Error", "Exist Username!")

def change_pass_functioin():
    change_tk = tk.Tk()
    change_tk.title("CHANGE PASS")
    change_tk.geometry("300x300")

    tk.Label(change_tk, text='username', font=('Arial', 15)).pack(anchor="w")
    user_change = tk.Entry(change_tk, font=('Arial', 15))
    user_change.pack()

    tk.Label(change_tk, text='2fa code', font=('Arial', 15)).pack(anchor="w")
    auth_code = tk.Entry(change_tk, font=('Arial', 15))
    auth_code.pack()

    tk.Label(change_tk, text='new password', font=('Arial', 15)).pack(anchor="w")
    new_pass = tk.Entry(change_tk, font=('Arial', 15))
    new_pass.pack()

    tk.Button(
        change_tk, text='Done', font=('Arial', 15), 
        command=lambda: done_change(user_change, auth_code, new_pass, change_tk)
        ).pack(padx=50, pady=20)

    change_tk.mainloop()

def done_change(user_change, auth_code, new_pass, change_tk):
    user = user_change.get().strip()
    newpass = new_pass.get().strip()
    facode = auth_code.get().strip()

    dt = pd.read_csv("dulieu.csv")
    user_data = dt[dt['username']==user]

    if (user_data["auth_code"]==int(facode)).any():
        dt.loc[dt["username"]==user, "passw"] = newpass

    dt.to_csv("dulieu.csv", index=False)
    messagebox.showinfo("Information", "DONE")
    change_tk.destroy()


tk.Label(window, text='username', font=('Arial', 15)).grid(row=0, column=0, padx=20)
user_entry = tk.Entry(window, font=('Arial', 15))
user_entry.grid(row=0, column=1)

tk.Label(window, text='password', font=('Arial', 15)).grid(row=1, column=0, padx=20, pady=20)
pass_entry = tk.Entry(window, font=('Arial', 15))
pass_entry.grid(row=1, column=1, pady=20)

tk.Label(window, text='2fa code', font=('Arial', 15)).grid(row=2, column=0, padx=20, pady=20)
facode_entry = tk.Entry(window, font=('Arial', 15))
facode_entry.grid(row=2, column=1, pady=20)

login_button = tk.Button(window, text="Login", font=('Arial', 15), command=login_function)
login_button.grid(row=3, column=1, padx=(0,100))

reg_button = tk.Button(window, text="Reg", font=('Arial', 15), command=reg_function)
reg_button.grid(row=3, column=2, padx=10)

reg_button = tk.Button(window, text="Change Pass", font=('Arial', 15), command=change_pass_functioin)
reg_button.grid(row=4, column=1, pady=40, padx=(100,0))

window.mainloop()