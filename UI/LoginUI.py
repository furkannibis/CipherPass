from tkinter import *
from UI.DialogUI import Message
from PASS.Password import PasswordManager

class LoginUI(Tk):
    def __init__(self):
        super().__init__()
        
        self.passM = PasswordManager()
        
        self.q_title = ''
        self.message =  ''
    
        self.messageBox = Message(self)
        self.user_can_pass = False
        
        self.TITLE_FONT = ('Arial', 28, 'bold')
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
        
        # Labels
        username_label = Label(text='Username: ', font=self.FONT)
        username_label.grid(column=0, row=1)
        
        password_label = Label(text='Password: ', font=self.FONT)
        password_label.grid(column=0, row=2)
        
        # Entries
        self.username_entry = Entry()
        self.username_entry.grid(column=1, row=1)
        
        self.password_entry = Entry(show='*')
        self.password_entry.grid(column=1, row=2)
        
        # Buttons
        login_button = Button(text='Login', command=self.check_input, width=15)
        login_button.grid(column=0, columnspan=2, row=3)
        
        self.mainloop()

    def check_input(self):
        if self.username_entry.get() == '' or self.password_entry.get() == '':
            self.q_title = 'Check your inputs.'
            self.message = 'Please make sure that you do not leave the username and password entries blank.'
            self.show_err()
            
        elif not self.passM.check_key_file() and not self.passM.check_pass_file():
            self.q_title = 'Welcome to CipherPass 🔐'
            self.message = 'It looks like this is your first time logging into CipherPass. CipherPass will use the values ​​you have currently entered as username and password. Confirm?'
            self.ask_q()
            
            if self.usr_answer:
                self.passM.generate_file_dir()
                self.passM.generate_key_file()
                self.passM.generate_pass_file()
                
                self.passM.add_pass_file(app='cipherpass', username=self.username_entry.get(), password=self.password_entry.get())
                
                self.user_can_pass = True
                
                self.quit()
                self.destroy()
            else:
                self.q_title = 'Bye 👋🏻'
                self.message = 'Okay, never mind. See you later..👋🏻'
                self.say_goodby()
                self.quit()
                self.destroy()
        else:
            if self.passM.check_cipherpass(username=self.username_entry.get(), password=self.password_entry.get()):
                self.user_can_pass = True
                self.quit()
                self.destroy()

            else:
                self.q_title = 'Wrong username or password.'
                self.message = 'Wrong username or password please check your entries again!'
                self.show_err()

    def ask_q(self):
        self.usr_answer = self.messageBox.ask_question(self.q_title, self.message)

    def show_err(self):
        self.usr_answer = self.messageBox.send_err_notification(self.q_title, self.message)
        
    def say_goodby(self):
        self.usr_answer = self.messageBox.send_normal_notification(self.q_title, self.message)