import tkinter
import login

root = tkinter.Tk()
root.title("Balls")
root.resizable(width=False, height=False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


class frame_login:
    def __init__(self, success_menu_class):
        self.background_colour = '#131313'
        self.frame_visibility = False
        self.success_menu_class = success_menu_class

        self.frame = tkinter.Frame(root, background=self.background_colour)
        self.label_user = tkinter.Label(self.frame, text="Username:", background=self.background_colour, foreground='white')
        self.label_pass = tkinter.Label(self.frame, text="Password:", background=self.background_colour, foreground='white')
        self.entry_user = tkinter.Entry(self.frame, width=25, border=3, background=self.background_colour,
                                        foreground='white')
        self.entry_pass = tkinter.Entry(self.frame, width=25, border=3, background=self.background_colour,
                                        foreground='white')
        self.b1 = tkinter.Button(self.frame, text="Login", width=20, height=1, background=self.background_colour,
                                 foreground='white', command=self.login_info_check)

    def show_frame(self):
        if not self.frame_visibility:
            self.frame.grid(row=0, column=0)

            self.label_user.grid(row=0, column=0, pady=2)
            self.label_pass.grid(row=1, column=0, pady=2)

            self.entry_user.grid(row=0, column=1, pady=2)
            self.entry_pass.grid(row=1, column=1, pady=2)

            self.b1.grid(row=2, column=1, pady=2)

            self.frame_visibility = True

    def hide_frame(self):
        if self.frame_visibility:
            self.frame_visibility = False
            self.frame.grid_forget()

    def login_info_check(self):
        database_name = 'logins.db'
        login_attempt = login.Login_Interfaces(database_name)
        login_result = login_attempt.login_gui_bool(username=self.entry_user.get(), password=self.entry_pass.get())

        if login_result:
            print("success")
            login_menu.hide_frame()
            self.success_menu_class.show_frame()

        if not login_result: print("fail")


class frame_menu:
    def __init__(self, success_menu_class = None):
        self.background_colour = '#131313'
        self.frame_visibility = False
        self.success_menu_class = success_menu_class

        self.frame = tkinter.Frame(root, background=self.background_colour)
        self.label_welcome = tkinter.Label(self.frame, text="Welcome!", background=self.background_colour,
                                        foreground='white', width=20)

    def show_frame(self):
        if not self.frame_visibility:
            self.frame.grid(row=0, column=0)

            self.label_welcome.grid(row=0, column=0, pady=0)

            self.frame_visibility = True

    def hide_frame(self):
        if self.frame_visibility:
            self.frame_visibility = False
            self.frame.grid_forget()


after_menu = frame_menu()

login_menu = frame_login(after_menu)
login_menu.show_frame()

root.mainloop()