
# 🔒 Password Manager 

A simple **Password Manager** script that allows you to securely store, update, and delete passwords for different accounts.

---

## 🚀 Features

- 🔑 **Securely store passwords** in a local file.  
- 📄 **View saved passwords** easily.  
- ✏️ **Update existing passwords** when needed.  
- ❌ **Delete old passwords** for accounts you no longer use.  
- 🛠️ **Master password protection** for basic security.  

---

## 🛠️ Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
   ```

2. **Run the script:**  
   ```bash
   python password_manager.py
   ```

---

## 🔹 How It Works

1. **Enter a Master Password** when prompted.  
2. **Choose an option:**  
   - `add` → Add a new account password.  
   - `view` → Display all stored passwords.  
   - `update` → Modify an existing password.  
   - `delete` → Remove an account password.  
   - `q` → Quit the program.  
3. **Passwords are stored in `passwords.txt`** in a simple `account | password` format.

---

## ⚠️ Important Notes

- This script **does not encrypt** passwords. For better security, consider using hashing or encryption (e.g., `cryptography` or `bcrypt` libraries).
- Ensure that **`passwords.txt`** is stored securely and not accessible by unauthorized users.

---

## 🤝 Contributing

Got ideas for improvements? Feel free to **fork** this repository and submit a Pull Request!

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

This project is no longer being updated
