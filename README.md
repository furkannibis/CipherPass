# CipherPass 🔐

CipherPass is an advanced, secure password management system built using Python and Tkinter for a simple, user-friendly interface. By leveraging encryption through the `cryptography` library, CipherPass ensures that all your sensitive information is safely stored, encrypted, and retrievable only by you.

The project features an elegant and easy-to-use GUI that allows users to securely add, find, and manage passwords for various applications, ensuring they never lose track of important credentials. The system is perfect for those who value both security and simplicity.

## Features ✨

- **First-time user setup**: On initial use, CipherPass prompts the user to set up their credentials securely. These are encrypted and stored using industry-standard cryptography techniques.
- **Encrypted storage**: CipherPass securely encrypts both the passwords and the username using the `cryptography.fernet` module. All data is saved in a protected file that only CipherPass can decrypt.
- **Add new credentials**: Easily add new passwords for any application, complete with username and password. These are encrypted and stored securely within the system.
- **Find stored credentials**: Quickly search for and retrieve stored usernames or passwords for any application. The system offers convenient options to copy credentials directly to your clipboard for easy use.
- **Clipboard support**: With built-in support for clipboard operations, CipherPass allows you to copy any retrieved username or password with a single click.
- **Error handling and notifications**: Built-in dialog notifications inform users of any errors (such as empty fields or incorrect login attempts), making the user experience smooth and informative.
- **Security-first approach**: Every interaction with the password file is secured with encryption. The decryption key is stored separately, ensuring the highest level of protection for your credentials.

## Technical Details 🔧

CipherPass is built with a focus on both security and ease of use:

- **Tkinter GUI**: Provides an intuitive, simple interface for users to interact with the system, allowing for smooth navigation and an easy learning curve.
- **Cryptography with `Fernet`**: Ensures that all stored passwords are encrypted using `Fernet` symmetric encryption, making sure your data is safe from unauthorized access.
- **File system structure**: CipherPass organizes and encrypts its files in a hidden `.pass` directory, separating the encryption key and the encrypted passwords into different files for enhanced security.
- **Cross-platform compatibility**: Runs seamlessly on Windows, macOS, and Linux thanks to Python’s cross-platform nature.

## Project Structure 📂

```plaintext
CipherPass/
│
├── PASS/
│   ├── Password.py          # Handles password encryption, decryption, and file management
│   ├── Copy.py              # Manages clipboard operations for copying passwords and usernames
│
├── UI/
│   ├── LoginUI.py           # Contains the logic for the login interface
│   ├── MainUI.py            # Contains the logic for the main password management interface
│   ├── DialogUI.py          # Manages all user notifications, questions, and error prompts
│
├── .pass/                   # Hidden directory where encrypted credentials are stored
│   ├── .filekey.key         # The key used for encryption and decryption of passwords
│   ├── .pass.txt            # The file containing encrypted credentials
│
└── main.py                  # The main entry point for launching CipherPass
```

## How It Works 🛠️

### 1. First-Time Setup:
If you are a first-time user, CipherPass will detect that no credentials exist and prompt you to set up your username and password. This information will be encrypted and stored securely for future use.

### 2. Adding a Password:
Users can easily add new credentials for any application by filling in the relevant fields (Application name, Username, and Password). Once added, the information is securely encrypted and stored, ready to be retrieved when needed.

### 3. Retrieving Credentials:
To retrieve stored information, simply input the application name, and CipherPass will provide the associated username or password. You can then copy the data to your clipboard for easy access.

### 4. Security Mechanisms:
- All sensitive data is encrypted using the `Fernet` encryption method.
- The encryption key is stored separately from the encrypted data for enhanced security.
- All password retrievals require confirmation to ensure they are being accessed by the correct user.

## Installation & Usage 🖥️

### Prerequisites:
- pip install -r requipments.txt

### Installation:

1. Clone this repository:

   ```bash
   git clone https://github.com/furkannibis/CipherPass.git
   cd CipherPass
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Security Notes 🔐

CipherPass takes a security-first approach by encrypting all data. However, it is essential to keep the `.filekey.key` safe and not share it. Losing this file will result in being unable to decrypt the stored credentials, rendering them inaccessible.

## Contributions 💻

Contributions are always welcome! Whether it's fixing bugs, adding new features, or improving documentation, feel free to submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

With CipherPass, managing and securing your passwords has never been easier. It combines the simplicity of a straightforward interface with robust encryption to protect your data from unauthorized access. Try it out today and say goodbye to forgotten passwords forever!

