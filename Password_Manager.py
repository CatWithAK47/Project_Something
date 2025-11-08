import json as jn
import tkinter as tk
from tkinter import simpledialog
from cryptography.fernet import Fernet
import csv
import os

window = tk.Tk()
window.title("Password Manager")  
window.geometry("500x650")
window.resizable(False, False)

listbox = tk.Listbox(window)
listbox.config(width=60, height=20)
listbox.pack(pady=20)

key_filename = "secret_key.key"

# Check if key file exists, if not create one

if os.path.exists('secret_key.key'):
    with open('secret_key.key', 'rb') as key_file:
        fernet_key = key_file.read()
        print(fernet_key)
else:
    fernet_key = Fernet.generate_key()
    with open('secret_key.key', 'wb') as key_file:
        key_file.write(fernet_key)

fernet = Fernet(fernet_key)

# Load existing passwords

password_list = {}

with open('encrypted_passwords.csv', 'r') as f:
    encrypted_data = f.read().strip()
    print(encrypted_data)

json_encrypted_data = jn.dumps(encrypted_data)
encrypted_json = fernet.encrypt(json_encrypted_data.encode('utf-8'))
decrypted_data = fernet.decrypt(encrypted_json).decode('utf-8')
        
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
    dis_ind = selected_indices[0]
    username, password =  password_list[listbox.get(dis_ind)]
    tk.messagebox.showinfo("Content", f"App Name: {listbox.get(dis_ind)}\nUsername: {username}\nPassword: {password}")

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
    json_encrypted_data = jn.dumps(encrypted_data)
    encrypted_json = fernet.encrypt(json_encrypted_data.encode('utf-8'))
    
    with open('encrypted_passwords.csv', 'w', newline='') as f:
        f.write(str(encrypted_json))

    print(fernet.decrypt(encrypted_json).decode('utf-8'))

    print("Passwords Saved Successfully.")

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
list = [1, 2, 3, 4, 5]

list_squared = [i ** 2 for i in list]

print(list_squared)

