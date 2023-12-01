import tkinter
from tkinter import *
import login


class Frame_Login_Page(Frame):
    def __init__(self, parent, controller):
        self.background_colour = '#131313'
        self.background_colour_highlight = '#292929'

        Frame.__init__(self, parent, bg=self.background_colour)

        self.parent = parent
        self.controller = controller

        self.second_frame = Frame(self, bg=self.background_colour)
        self.label_user = Label(self.second_frame, text="Username:", background=self.background_colour,
                                foreground='white')
        self.label_pass = Label(self.second_frame, text="Password:", background=self.background_colour,
                                foreground='white')
        self.label_user_status = Label(self.second_frame, background=self.background_colour, foreground='white')

        self.entry_user = Entry(self.second_frame, width=25, border=3, background=self.background_colour,
                                foreground='white', relief=FLAT, highlightthickness=0)
        self.entry_pass = Entry(self.second_frame, width=25, border=3, background=self.background_colour,
                                foreground='white', show="*", relief=FLAT, highlightthickness=0)

        self.line_user = Canvas(self.second_frame, width=150, height=1.0, bg="white", highlightthickness=0)
        self.line_pass = Canvas(self.second_frame, width=150, height=1.0, bg="white", highlightthickness=0)

        self.b1 = Button(self.second_frame, text="Login", width=20, height=1, background=self.background_colour,
                         foreground='white', command=self.login_info_check, relief=FLAT, overrelief=RAISED)
        self.b2 = Button(self.second_frame, text='Create login', width=12, height=1, background=self.background_colour,
                         foreground='white', relief=FLAT, overrelief=RAISED)

        self.pack_widgets()

    def grid_widgets(self):
        self.label_user.grid(row=0, column=0, pady=10)
        self.label_pass.grid(row=1, column=0, pady=10)

        self.entry_user.grid(row=0, column=1, pady=10)
        self.entry_pass.grid(row=1, column=1, pady=10)

        self.line_user.grid(row=0, column=1, pady=10, sticky="s")
        self.line_pass.grid(row=1, column=1, pady=10, sticky="s")

        self.b1.grid(row=3, column=1, pady=10)
        self.b2.grid(row=3, column=0, pady=10)

    def pack_widgets(self):
        self.second_frame.pack(expand=True, anchor="center")
        self.grid_widgets()

    def login_info_check(self):
        database_name = 'logins.db'
        login_attempt = login.Login_Interfaces(database_name)
        login_result = login_attempt.login_gui_bool(username=self.entry_user.get(), password=self.entry_pass.get())
        self.label_user_status.grid_forget()

        if login_result:
            if (self.entry_user.get() == "admin") and True:
                self.entry_user.delete(0, 'end')
                self.entry_pass.delete(0, 'end')
                pass
            else:
                self.controller.show_frame("Frame_Welcome_Page")
                self.entry_user.delete(0, 'end')
                self.entry_pass.delete(0, 'end')

        elif not login_result:
            self.label_user_status.grid(row=2, columnspan=2, pady=2)
            self.label_user_status["text"] = "Username or password is incorrect."


class Frame_Welcome_Page(Frame):
    def __init__(self, parent, controller):
        self.background_colour = '#131313'
        Frame.__init__(self, parent, bg=self.background_colour)
        self.parent = parent
        self.controller = controller

        self.second_frame = Frame(self, bg=self.background_colour)
        self.label_welcome = Label(self.second_frame, text="Welcome!", background=self.background_colour,
                                   foreground='white', width=20)
        self.logout_button = Button(self.second_frame, text="Log Out", background=self.background_colour, fg="white",
                                    command=self.back_to_login, width=10, relief=FLAT, overrelief=RAISED)
        self.pack_widgets()

    def grid_widgets(self):
        self.label_welcome.grid(row=0, columnspan=1, pady=10)
        self.logout_button.grid(row=1, column=0, pady=10)

    def pack_widgets(self):
        self.second_frame.pack(expand=True, anchor="center")
        self.grid_widgets()

    def back_to_login(self):
        self.controller.show_frame("Frame_Login_Page")


class MainW(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.resizable(height=False, width=False)
        self.geometry("500x250")
        self.parent = parent

        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Frame_Login_Page, Frame_Welcome_Page):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Frame_Login_Page")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainW(None)
    app.mainloop()
    
