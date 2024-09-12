from tkinter import *
import tkinter.messagebox  as mb

class Message(Tk):
    def __init__(self, parent):
        self.parent = parent
    
    def ask_question(self, title, message):
        return mb.askyesno(title=title, message=message)
    
    def send_err_notification(self, title, message):
        return mb.showerror(title=title, message=message)
    
    def send_normal_notification(self, title, message):
        return mb.showinfo(title=title, message=message)