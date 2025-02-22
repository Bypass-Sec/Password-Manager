import os
import tkinter as tk
from tkinter import simpledialog, messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("400x300")
        self.master.configure(bg='#f0f0f0')

        self.password_file = "passwords.txt"

        # Ensure the file exists
        if not os.path.exists(self.password_file):
            with open(self.password_file, "w") as f:
                pass

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Password Manager", font=("Arial", 20), bg='#f0f0f0').pack(pady=10)

        tk.Button(self.master, text="View Passwords", command=self.view, width=20).pack(pady=5)
        tk.Button(self.master, text="Add Password", command=self.add, width=20).pack(pady=5)
        tk.Button(self.master, text="Update Password", command=self.update, width=20).pack(pady=5)
        tk.Button(self.master, text="Delete Password", command=self.delete, width=20).pack(pady=5)
        tk.Button(self.master, text="Quit", command=self.master.quit, width=20).pack(pady=5)

    def view(self):
        with open(self.password_file, 'r') as f:
            passwords = f.read()
        if passwords:
            messagebox.showinfo("Saved Passwords", passwords)
        else:
            messagebox.showinfo("Saved Passwords", "No passwords saved yet.")

    def add(self):
        name = simpledialog.askstring("Add Password", "Account Name:")
        if name:
            pwd = simpledialog.askstring("Add Password", "Password:", show='*')
            if pwd:
                with open(self.password_file, 'a') as f:
                    f.write(f"{name} | {pwd}\n")
                messagebox.showinfo("Success", "Password added successfully.")

    def update(self):
        account = simpledialog.askstring("Update Password", "Enter account name to update:")
        if account:
            new_pwd = simpledialog.askstring("Update Password", "Enter new password:", show='*')
            if new_pwd:
                lines = []
                with open(self.password_file, 'r') as f:
                    lines = f.readlines()
                with open(self.password_file, 'w') as f:
                    updated = False
                    for line in lines:
                        if line.startswith(account + ' |'):
                            f.write(f"{account} | {new_pwd}\n")
                            updated = True
                        else:
                            f.write(line)
                if updated:
                    messagebox.showinfo("Success", "Password updated successfully.")
                else:
                    messagebox.showwarning("Not Found", "Account not found.")

    def delete(self):
        account = simpledialog.askstring("Delete Password", "Enter account name to delete:")
        if account:
            lines = []
            with open(self.password_file, 'r') as f:
                lines = f.readlines()
            with open(self.password_file, 'w') as f:
                deleted = False
                for line in lines:
                    if not line.startswith(account + ' |'):
                        f.write(line)
                    else:
                        deleted = True
            if deleted:
                messagebox.showinfo("Success", "Password deleted successfully.")
            else:
                messagebox.showwarning("Not Found", "Account not found.")

if __name__ == "__main__":
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()

