from UI.LoginUI import LoginUI
from UI.MainUI import MainUI

loginUI = LoginUI()

if loginUI.user_can_pass:
    mainUI = MainUI()
