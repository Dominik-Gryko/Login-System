import tkinter
import login

root = tkinter.Tk()
root.title("Login System")
root.resizable(width=False, height=False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


class frame_login:
    def __init__(self, success_menu_class, create_login_menu_class):
        self.background_colour = '#131313'
        self.frame_visibility = False
        self.success_menu_class = success_menu_class
        self.create_login_menu_class = create_login_menu_class

        self.frame = tkinter.Frame(root, background=self.background_colour)
        self.label_user = tkinter.Label(self.frame, text="Username:", background=self.background_colour,
                                        foreground='white')
        self.label_pass = tkinter.Label(self.frame, text="Password:", background=self.background_colour,
                                        foreground='white')
        self.label_user_status = tkinter.Label(self.frame, background=self.background_colour, foreground='white')
        self.entry_user = tkinter.Entry(self.frame, width=25, border=3, background=self.background_colour,
                                        foreground='white')
        self.entry_pass = tkinter.Entry(self.frame, width=25, border=3, background=self.background_colour,
                                        foreground='white', show="*")
        self.b1 = tkinter.Button(self.frame, text="Login", width=20, height=1, background=self.background_colour,
                                 foreground='white', command=self.login_info_check)
        self.b2 = tkinter.Button(self.frame, text='Create login', width=12, height=1, background=self.background_colour,
                                 foreground='white', command=self.create_login_page)

    def show_frame(self):
        if not self.frame_visibility:
            self.frame.grid(row=0, column=0)

            self.label_user.grid(row=0, column=0, pady=2)
            self.label_pass.grid(row=1, column=0, pady=2)

            self.entry_user.grid(row=0, column=1, pady=2)
            self.entry_pass.grid(row=1, column=1, pady=2)

            self.b1.grid(row=3, column=1, pady=2)
            self.b2.grid(row=3, column=0, pady=2)

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
            self.hide_frame()
            self.success_menu_class.show_frame()

        if not login_result:
            self.label_user_status.grid(row=2, columnspan=2, pady=2)
            self.label_user_status["text"] = "Username or password is incorrect."

    def create_login_page(self):
        self.frame.destroy()
        self.create_login_menu_class.show_frame()


class frame_menu:
    def __init__(self, success_menu_class=None):
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


class frame_menu_create_login:
    def __init__(self, back_menu_class=None):
        self.background_colour = '#131313'
        self.frame_visibility = False
        self.back_menu_class = back_menu_class

        self.frame = tkinter.Frame(root, background=self.background_colour)
        self.label_user = tkinter.Label(self.frame, text="Username:", background=self.background_colour,
                                        foreground='white')
        self.label_pass = tkinter.Label(self.frame, text="Password:", background=self.background_colour,
                                        foreground='white')
        self.label_pass2 = tkinter.Label(self.frame, text="Confirm Password:", background=self.background_colour,
                                         foreground='white')
        self.label_user_status = tkinter.Label(self.frame, background=self.background_colour, foreground='white')
        self.entry_user = tkinter.Entry(self.frame, width=25, border=3, background=self.background_colour,
                                        foreground='white')
        self.entry_pass = tkinter.Entry(self.frame, width=25, border=3, background=self.background_colour,
                                        foreground='white', show="*")
        self.entry_pass2 = tkinter.Entry(self.frame, width=25, border=3, background=self.background_colour,
                                         foreground='white', show="*")
        self.b1 = tkinter.Button(self.frame, text="Create Login", width=20, height=1, background=self.background_colour,
                                 foreground='white', command=self.create_login)
        self.b2 = tkinter.Button(self.frame, text="Back", width=12, height=1, background=self.background_colour,
                                 foreground="white", command=self.back)

    def show_frame(self):
        if not self.frame_visibility:
            self.frame.grid(row=0, column=0)

            self.label_user.grid(row=0, column=0, pady=2)
            self.label_pass.grid(row=1, column=0, pady=2)
            self.label_pass2.grid(row=2, column=0, pady=2)

            self.entry_user.grid(row=0, column=1, pady=2)
            self.entry_pass.grid(row=1, column=1, pady=2)
            self.entry_pass2.grid(row=2, column=1, pady=2)

            self.b1.grid(row=4, column=1, pady=2)
            self.b2.grid(row=4, column=0, pady=2)

            self.frame_visibility = True

    def hide_frame(self):
        if self.frame_visibility:
            self.frame_visibility = False
            self.frame.grid_forget()

    def back(self):
        if self.back_menu_class is not None:
            self.hide_frame()
            self.back_menu_class.show_frame()

        else:
            try:
                self.hide_frame()
                login_menu.show_frame()
            except Exception:
                pass

    def create_login(self):
        database_name = 'logins.db'
        login_attempt = login.Login_Interfaces(database_name)

        if self.entry_pass.get() == self.entry_pass2.get():
            self.label_user_status.grid_forget()
            login_result = login_attempt.login_gui_bool(username=self.entry_user.get(), password=self.entry_pass.get())

            if login_result:
                self.label_user_status.grid(row=3, columnspan=2, pady=2)
                self.label_user_status["text"] = "User already exists. Use a different username."

            if not login_result:
                login_attempt.create_login_gui(username=self.entry_user.get(), password=self.entry_pass.get())
                self.label_user_status.grid(row=3, columnspan=2, pady=2)
                self.label_user_status["text"] = "Success: User was now created."
        else:
            self.label_user_status.grid(row=3, columnspan=2, pady=2)
            self.label_user_status["text"] = "Passwords dont match. Please try again."


after_menu = frame_menu()
create_login_menu = frame_menu_create_login()

login_menu = frame_login(after_menu, create_login_menu)
login_menu.show_frame()

root.mainloop()
