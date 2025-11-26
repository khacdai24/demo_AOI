import tkinter as tk
import csv
import tkinter.messagebox as messagebox
import os

def enter_data_function():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    email = email_entry.get().strip()
    
    if name == "" or age == "" or email == "": 
        messagebox.showerror("Error", "Please Fill Information")
        return

    checkfile = os.path.isfile("dulieu1.csv")
    with open("dulieu1.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not checkfile:
            writer.writerow(["Name", "Age", "Email"])
        
        writer.writerow([name, age, email])
    
    messagebox.showinfo("Infomation", "Save Data Successfully")
    
    return 

window = tk.Tk()
window.title("Save data")
window.geometry("600x600")

tk.Label(window, text="Name", fg="white", bg="limegreen", font=("Arial", 15)).pack(anchor="w", padx=100)
name_entry = tk.Entry(window, width=20, font=("Arial", 15))
name_entry.pack(padx=20, pady=0)

tk.Label(window, text="Age", fg="white", bg="limegreen", font=("Arial", 15)).pack(anchor="w", padx=100)
age_entry = tk.Entry(window, width=20, font=("Arial", 15))
age_entry.pack(padx=20, pady=0)

tk.Label(window, text="Email", fg="white", bg="limegreen", font=("Arial", 15)).pack(anchor="w", padx=100)
email_entry = tk.Entry(window, width=20, font=("Arial", 15))
email_entry.pack()
    
save_button = tk.Button(window, text="Enter", fg="white", bg="cyan", font=("Arial", 15), command=enter_data_function)
save_button.pack(pady=20)

window.mainloop()
