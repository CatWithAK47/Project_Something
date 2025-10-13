import json as jn
import tkinter as tk
from tkinter import simpledialog
import winsound

window = tk.Tk()
window.title("Password Manager")  
window.geometry("500x650")
window.resizable(False, False)

listbox = tk.Listbox(window, selectmode=tk.EXTENDED)
listbox.config(width=60, height=20)
listbox.pack(pady=20)

try:
    with open("password_list.json", 'r') as f:
        password_list = jn.load(f)
except:
    password_list = {}

listbox.delete(0, tk.END)
for item in password_list:
    listbox.insert(tk.END, item)

password_list_keys = list(password_list.keys())

# Gui Functions
def display_content():
    selected_indices = listbox.curselection()

    if not selected_indices:
        tk.messagebox.showinfo("Content", "No item selected.")
        return
        
    
    del_ind = selected_indices[0]
    tk.messagebox.showinfo("Content", password_list[listbox.get(del_ind)])

def add():
    app = simpledialog.askstring(title="App Name Popup",
                                  prompt="What is App Name? ")
    
    username = simpledialog.askstring(title="Username Popup",
                                  prompt="What is Your Username? ")
    
    password = simpledialog.askstring(title="Password Popup",
                                  prompt="What's Your Password? ")
    
    if app == None:
        return


    password_list[app] = username, password
    listbox.insert(tk.END, app)

def save():

    print("Saving passwords...")
    with open("password_list.json", "w") as f:
            jn.dump(password_list, f)

def lremove():
    selected_indices = listbox.curselection()
    password_list_keys = list(password_list.keys())

    if not selected_indices:
        tk.messagebox.showinfo("Content", "No item selected.")
        return

    del_ind = selected_indices[0]

    print(listbox.get(del_ind))

    listbox.delete(del_ind)

    del password_list[password_list_keys[del_ind]]

    print(del_ind)

def quit():
    save()
    print("Quitting...")
    try:
        window.destroy()
        exit()
    except:
        exit()

# GUI Buttons
tk.Button(window, text="Add Password", command=add).pack(pady=10)
tk.Button(window, text="Save Passwords", command=save).pack(pady=10)
tk.Button(window, text="Remove Current Item", command=lremove).pack(pady=10)
tk.Button(window, text="Display Current Item", command=display_content).pack(pady=10)
tk.Button(window, text="Quit", command=quit).pack(pady=10)

window.mainloop()