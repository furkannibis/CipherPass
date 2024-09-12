from tkinter import *
from PASS.Password import PasswordManager
from PASS.Copy import copy_text
from UI.DialogUI import Message


class MainUI(Tk):
    def __init__(self):
        super().__init__()
        self.passM = PasswordManager()
        self.messageBox = Message(self)
        self.q_title = ''
        self.message =  ''
        
        self.TITLE_FONT = ('Arial', 28, 'bold')
        self.SUB_TITLE_FONT = ('Arial', 14, 'bold')
        self.FONT = ('Arial', 14, 'italic')

        self.title('CipherPass')
        self.config(padx=50, pady=50)
        
        # Images
        image = PhotoImage(file='UI/logo.png')
        
        # Canvas
        logo_canvas = Canvas(width=250, height=250)
        logo_canvas.create_image(125, 125, image=image)
        logo_canvas.create_text(125, 175, text='CipherPass', font=self.TITLE_FONT)
        logo_canvas.grid(column=0, columnspan=2, row=0)
        
        # Label
        add_pass_label = Label(text='Add new password to CipherPass 🔒', font=self.SUB_TITLE_FONT)
        add_pass_label.grid(column=0, columnspan=2, row=1)
        
        add_pass_app_label = Label(text='Application:', font=self.FONT)
        add_pass_app_label.grid(column=0, row=2)
        
        add_pass_username_label = Label(text='Username:', font=self.FONT)
        add_pass_username_label.grid(column=0, row=3)
        
        add_pass_password_label = Label(text='Password:', font=self.FONT)
        add_pass_password_label.grid(column=0, row=4)
        
        find_pass_label = Label(text='Find your password from CipherPass 🔒', font=self.SUB_TITLE_FONT)
        find_pass_label.config(pady=20)
        find_pass_label.grid(column=0, columnspan=2, row=6)
        
        find_username_password_label = Label(text='Application:', font=self.FONT)
        find_username_password_label.grid(column=0, row=7)
        
        # Entries
        self.add_pass_app_entry = Entry()
        self.add_pass_app_entry.grid(column=1, row=2)
        
        self.add_pass_username_entry = Entry()
        self.add_pass_username_entry.grid(column=1, row=3)
        
        self.add_pass_password_entry = Entry(show='*')
        self.add_pass_password_entry.grid(column=1, row=4)
        
        self.find_username_password_entry = Entry()
        self.find_username_password_entry.grid(column=1, row=7)
        
        # Buttons
        add_password = Button(text='Add to CipherPass 🔏', command=self.add_pass)
        add_password.grid(column=0, columnspan=2, row=5)
        
        find_username = Button(text='Find username from CipherPass 🔏', command=self.find_username)
        find_username.grid(column=0, row=8)
        
        find_password = Button(text='Find password from CipherPass 🔏', command=self.find_password)
        find_password.grid(column=1, row=8)
        
        self.mainloop()
    
    def add_pass(self):
        if self.add_pass_app_entry.get != '' and self.add_pass_username_entry.get() != '' and self.add_pass_password_entry.get() != '':
            self.passM.add_pass_file(app=self.add_pass_app_entry.get(), username=self.add_pass_username_entry.get(), password=self.add_pass_password_entry.get())
            self.title = 'Password added.'
            self.message = 'The information you entered has been successfully added to CipherPass. 🔑'
            self.messageBox.send_normal_notification(title=self.title, message=self.message)
            
            self.add_pass_app_entry.delete(0, 'end')
            self.add_pass_username_entry.delete(0, 'end')
            self.add_pass_password_entry.delete(0, 'end')
        else:
            self.title = 'Blank information error.'
            self.message = 'Fill in all required fields so that CipherPass can save your password in the system. 🔑'
            self.messageBox.send_err_notification(title=self.title, message=self.message)
        
    def find_username(self):
        if self.find_username_password_entry.get() == '':
            self.title = 'Which one?'
            self.message = 'Which username do you want to know?'
            self.messageBox.send_normal_notification(title=self.title, message=self.message)
        else:
            username = self.passM.find_app_username(app=self.find_username_password_entry.get())
            if username:
                self.title = 'CipherPass is copying...'
                self.message = 'CipherPass has detected a username for the information you specified. It will allow you to copy it once. Confirm?'
                usr_answer = self.messageBox.ask_question(title=self.title, message=self.message)
                if usr_answer:
                    copy_text(username)
            else:
                self.title = 'Not Found!'
                self.message = 'No registered username was found for the application you are looking for.'
                self.messageBox.send_err_notification(title=self.title, message=self.message)
    
    def find_password(self):
        if self.find_username_password_entry.get() == '':
            self.title = 'Which one?'
            self.message = 'Which password do you want to know?'
            self.messageBox.send_normal_notification(title=self.title, message=self.message)
        else:
            password = self.passM.find_app_password(app=self.find_username_password_entry.get())
            if password:
                self.title = 'CipherPass is copying...'
                self.message = 'CipherPass has detected a password for the information you specified. It will allow you to copy it once. Confirm?'
                usr_answer = self.messageBox.ask_question(title=self.title, message=self.message)
                if usr_answer:
                    copy_text(password)
            else:
                self.title = 'Not Found!'
                self.message = 'No registered password was found for the application you are looking for.'
                self.messageBox.send_err_notification(title=self.title, message=self.message)
    