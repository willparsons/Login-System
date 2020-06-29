from tkinter import *
from login import Login


def submit(username: str, password: str):
    if not username.isalnum() or not password.isalnum():
        print("Invalid data")
        return

    Login.login(username, password)


class GUI:
    def __init__(self):
        self.WIDTH = 640
        self.HEIGHT = 480

        self.BG = "#2e3336"
        self.ENTRY_BG = "#363636"

        self.root = Tk()
        self.root.title("Login")
        self.root.resizable(False, False)

    def run(self):
        canvas = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        canvas.pack()

        frame = Frame(self.root, bg=self.BG)

        user_label = Label(frame, text="Username:", bg=self.BG, fg="white")
        password_label = Label(frame, text="Password:", bg=self.BG, fg="white")

        user_entry = Entry(frame, bg=self.ENTRY_BG, fg="white", insertbackground="white")
        password_entry = Entry(frame, bg=self.ENTRY_BG, fg="white", insertbackground="white")

        login_button = Button(frame, text="Next", bg=self.BG, fg="white",
                              command=lambda: submit(user_entry.get(), password_entry.get()))

        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        user_label.place(relx=.4, rely=.35, anchor="center")
        password_label.place(relx=.4, rely=.45, anchor="center")
        user_entry.place(relx=.5, rely=.4, relwidth=.3, anchor="center")
        password_entry.place(relx=.5, rely=.5, relwidth=.3, anchor="center")
        login_button.place(relx=.5, rely=.58, relwidth=.1, anchor="center")

        self.root.mainloop()
