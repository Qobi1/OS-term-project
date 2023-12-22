from tkinter import *
from tkinter import messagebox
# import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)  # Replace with the server's IP address and port number
client_socket.connect(server_address)

ABOUT_TEXT = """ Here you can to find out which level to choose. Select your level, from A1 English level (elementary) to C1 English level (advanced), and improve your reading skills at your own speed, whenever it's convenient for you."""


class Authentification:

    def __init__(self, window):
        self.window = window
        self.window.geometry('925x500+300+200')
        self.window.configure(bg='#fff')
        self.window.resizable(False, False)
        self.window.title('HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM')
        self.img = PhotoImage(file='login.png')
        self.username = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()
        self.label = Label(self.window, image=self.img, border=0, bg='white')
        self.label.place(x=50, y=90)
        self.sign_up_frame = Frame(self.window, width=350, height=390, bg='#fff')
        self.sign_up_frame.place(x=480, y=50)
        self.create_sign_up_widgets()

        self.sign_in_frame = Frame(self.window, width=350, height=390, bg='#fff')
        # self.sign_in_frame.place(x=480, y=50)
        self.create_sign_in_widgets()

    def create_sign_up_widgets(self):

        heading = Label(self.sign_up_frame, text='Sign Up', fg='#57a1f8', bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 23, 'bold'))
        heading.place(x=100, y=10)

        user = Entry(self.sign_up_frame, width=25, fg='black', textvariable=self.username, border=0, bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 11))
        user.place(x=50, y=70)
        # user.insert(0, 'Username')
        user.bind("<FocusIn>", lambda event: self.on_enter(event, user))
        user.bind("<FocusOut>", lambda event: self.on_leave(event, user, 'Username'))
        Frame(self.sign_up_frame, width=295, height=2, bg='black').place(x=50, y=100)

        code = Entry(self.sign_up_frame, width=25, fg='black', textvariable=self.password, border=0, bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 11))
        code.place(x=50, y=140)
        # code.insert(0, 'Password')
        code.bind("<FocusIn>", lambda event: self.on_enter(event, code))
        code.bind("<FocusOut>", lambda event: self.on_leave(event, code, 'Password'))
        Frame(self.sign_up_frame, width=295, height=2, bg='black').place(x=50, y=170)

        conform_code = Entry(self.sign_up_frame, width=25, fg='black', textvariable=self.confirm_password, border=0, bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 11))
        conform_code.place(x=50, y=210)
        conform_code.insert(0, 'Confirm Password')
        conform_code.bind("<FocusIn>", lambda event: self.on_enter(event, conform_code))
        conform_code.bind("<FocusOut>", lambda event: self.on_leave(event, conform_code, 'Confirm Password'))
        Frame(self.sign_up_frame, width=295, height=2, bg='black').place(x=50, y=240)

        Button(self.sign_up_frame, width=42, pady=7, text="Sign Up", bg='#57a1f8', fg='white', border=0, command=self.sign_up).place(x=50, y=280)

        Button(self.sign_up_frame, text="Already have an account? Sign In", border=0, bg='white', cursor='hand2',
               fg='#57a1f8', command=self.show_sign_in).place(x=90, y=330)

    def create_sign_in_widgets(self):
        heading = Label(self.sign_in_frame, text='Sign In', fg='#57a1f8', bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 23, 'bold'))
        heading.place(x=100, y=5)

        user = Entry(self.sign_in_frame, width=25, fg='black', border=0, textvariable=self.username, bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind("<FocusIn>", lambda event: self.on_enter(event, user))
        user.bind("<FocusOut>", lambda event: self.on_leave(event, user, 'Username'))
        Frame(self.sign_in_frame, width=295, height=2, bg='black').place(x=30, y=110)

        code = Entry(self.sign_in_frame, width=25, fg='black', border=0, textvariable=self.password, bg='white', font=("HOUSECLEANING, PLUMBING, ELECTRICITY SERVICE & MAINTENANCE SYSTEM", 11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind("<FocusIn>", lambda event: self.on_enter(event, code))
        code.bind("<FocusOut>", lambda event: self.on_leave(event, code, 'Password'))
        Frame(self.sign_in_frame, width=295, height=2, bg='black').place(x=30, y=180)

        Button(self.sign_in_frame, width=39, pady=7, text="Sign In", bg='#57a1f8', fg='white', border=0, command=self.sign_in).place(x=35, y=230)
        Button(self.sign_in_frame, text="Don't have an account? Sign Up", border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.show_sign_up).place(x=80, y=280)

    def on_enter(self, e, command):
        command.delete(0, 'end')

    def on_leave(self, e, command, value):
        if command.get() == '':
            command.insert(0, value)

    def show_sign_in(self):
        self.sign_up_frame.place_forget()
        self.sign_in_frame.place(x=480, y=50)

    def show_sign_up(self):
        self.sign_in_frame.place_forget()
        self.sign_up_frame.place(x=480, y=50)

    def sign_up(self):
        username = self.username.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()
        message = f"""Insert into "user"(name, password) Values({username}, {password})"""
        client_socket.send(message.encode())
        # response = client_socket.recv(1024).decode()
        print(username, password, confirm_password)
        if password != 'Password' and username != 'Username' and confirm_password != 'Confirm Password':
            if password == confirm_password:
                messagebox.showinfo("Sign Up", f"Account created for {username}")
                User(self.window)
            else:
                messagebox.showinfo("Sign Up", f"Password doesn't match to each other. Please check again!")
        else:
            messagebox.showinfo("Sign Up", f"Username and/or Password cannot be blank")

    def sign_in(self):
        username = self.username.get()
        password = self.password.get()
        message = f'Select * from "user" where name == {username}'
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(response)

        if password != 'Password' and username != 'Username':
            if response['password'] == password and response['username'] == username and response['role'] == 'ADMIN':
                messagebox.showinfo("Sign In", f"Welcome back, {username}")
                self.label.place_forget()
                self.sign_in_frame.place_forget()
                AdminPanel(window)
            elif response['password'] == password and response['username'] == username and response['role'] == 'USER':
                messagebox.showinfo("Sign In", f"Welcome back, {username}")
                self.label.place_forget()
                self.sign_in_frame.place_forget()
                User(window)
        else:
            messagebox.showinfo("Sign In", f"Input values for Username and/or Password")


class AdminPanel:
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.options_frame = Frame(self.window, width=900, height=500, bg='#fff')
        self.main_frame = Frame(self.window, highlightbackground='black', highlightthickness=2)
        self.window.geometry('700x500+300+200')  # Delete after finishing
        self.window.resizable(False, False)  # Delete after finishing
        self.window.title('Welcome Admin')

        self.main_menu()

    def main_menu(self):
        self.options_frame.pack(side=LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=150, height=500, bg='#c3c3c3')
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500, width=900)
        welcome_msg = Label(self.main_frame, text='Welcome Admin', font=('Bold', 15))
        welcome_msg.place(x=200, y=10)
        service_list = Button(self.options_frame, width=12, text='Service List', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(service_list_indicate, self.service_page, extra_args))
        service_list.place(x=10, y=30)
        service_list_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        service_list_indicate.place(x=3, y=30, width=5, height=37)

        request_btn = Button(self.options_frame, width=12, text='Request List', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(request_indicate, self.request_page, extra_args))
        request_btn.place(x=10, y=80)
        request_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        request_indicate.place(x=3, y=80, width=5, height=37)

        client_btn = Button(self.options_frame, width=12, text='Clients', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(client_indicate, self.clients_page, extra_args))
        client_btn.place(x=10, y=130)
        client_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        client_indicate.place(x=3, y=130, width=5, height=37)

        setting_btn = Button(self.options_frame, width=12, text='Settings', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(setting_indicate, self.settings_page, extra_args))
        setting_btn.place(x=10, y=180)
        setting_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        setting_indicate.place(x=3, y=180, width=5, height=37)
        extra_args = (service_list_indicate, request_indicate, client_indicate, setting_indicate)

    def hide(self, args):
        for i in args:
            i.config(bg='#c3c3c3')

    def indicate(self, lb, page, args):
        self.hide(args)
        lb.config(bg='#158aff')
        page()

    def service_page(self):
        home_frame = Frame(self.main_frame, width=400, height=400)
        home_frame.place(x=50, y=50)
        Label(home_frame, text='ELECTRICITY SERVICE', font=('Bold', 12), justify='left').place(x=10, y=20)
        checkbox_state = BooleanVar()
        checkbox = Checkbutton(home_frame, text="Enable", variable=checkbox_state, command=lambda: get_value(checkbox_state, checkbox))
        checkbox.place(x=300, y=20)

        def get_value(value, button):
            if value.get():
                button.config(text='Disable')
            else:
                button.config(text='Enable')

    def request_page(self):
        request_frame = Frame(self.main_frame, width=400, height=400)
        request_frame.place(x=50, y=50)
        Label(request_frame, text='ELECTRICITY SERVICE', font=('Bold', 12), justify='left').place(x=10, y=20)
        Button(request_frame, text='View Details', command=lambda: view_detail()).place(x=300, y=20)

        def view_detail():
            detail = Frame(self.main_frame, width=400, height=400)
            detail.place(x=50, y=50)
            Label(detail, text='Service Type: ELECTRICITY SERVICE', font=('Bold', 12), justify='left').place(x=10, y=20)
            Label(detail, text='User: User 1', font=('Bold', 12), justify='left').place(x=10, y=40)
            Label(detail, text='DateTime: 12.12.2021 - 12 a.m.', font=('Bold', 12), justify='left').place(x=10, y=60)
            Button(detail, text='Back', command=lambda: self.request_page(), fg='white', bg='blue').place(x=10, y=120)

    def clients_page(self):
        home_frame = Frame(self.main_frame, width=400, height=400)
        home_frame.place(x=50, y=50)
        Label(home_frame, text='User 1(Created_at: 12.12.2021)', font=('Bold', 12), justify='left').place(x=10, y=20)

    def settings_page(self):
        settings_frame = Frame(self.main_frame, width=400, height=400)
        settings_frame.place(x=50, y=50)
        light = Button(settings_frame, text='Light mode', font=('Bold', 12), cursor='hand2', state='disabled',
                       command=lambda: light_mode(light, dark))
        light.place(x=20, y=20)
        dark = Button(settings_frame, text='Dark mode', font=('Bold', 12), cursor='hand2', state='active',
                      command=lambda: dark_mode(light, dark))
        dark.place(x=110, y=20)
        lb = Button(settings_frame, text='Log out', font=('Bold', 12), bg='blue', cursor='hand2', fg='white',
                    command=lambda: quit())
        lb.place(x=20, y=100)

        def quit():
            self.main_frame.destroy()
            self.options_frame.destroy()
            auth = Authentification(window).sign_up_frame
            return auth

        def light_mode(light, dark):
            light.configure(state='disabled')
            dark.configure(state='active')
            self.options_frame.configure(bg='#c3c3c3')

        def dark_mode(light, dark):
            light.configure(state='active')
            dark.configure(state='disabled')
            self.options_frame.configure(bg='#36585c')


class User:
    def __init__(self, window):
        self.window = window
        self.options_frame = Frame(self.window, width=900, height=500, bg='#fff')
        self.options_frame.pack(side=LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=150, height=500, bg='#c3c3c3')
        self.main_frame = Frame(self.window, highlightbackground='black', highlightthickness=2, width=500, height=600)
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500, width=900)
        self.window.geometry('700x500+300+200')  # Delete after finishing
        self.window.resizable(False, False)  # Delete after finishing
        self.window.title('Welcome User')
        self.main_menu()

    def main_menu(self):
        home_btn = Button(self.options_frame, text='Service List', width=12, font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(home_indicate, self.home_page, extra_args))
        home_btn.place(x=10, y=30)
        home_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        home_indicate.place(x=3, y=30, width=5, height=37)

        service_btn = Button(self.options_frame, text='History', width=12, font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(service_indicate, self.history_page, extra_args))
        service_btn.place(x=10, y=80)
        service_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        service_indicate.place(x=3, y=80, width=5, height=37)

        about_btn = Button(self.options_frame, text='About', width=12, font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(about_indicate, self.about_page, extra_args))
        about_btn.place(x=10, y=130)
        about_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        about_indicate.place(x=3, y=130, width=5, height=37)

        setting_btn = Button(self.options_frame, text='Settings', width=12, font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: self.indicate(setting_indicate, self.settings, extra_args))
        setting_btn.place(x=10, y=180)
        setting_indicate = Label(self.options_frame, text='', bg='#c3c3c3')
        setting_indicate.place(x=3, y=180, width=5, height=37)
        welcome_msg = Label(self.main_frame, text='Welcome User', font=('Bold', 15),)
        welcome_msg.place(x=200, y=10)
        extra_args = (home_indicate, service_indicate, about_indicate, setting_indicate)

    def hide(self, args):
        for i in args:
            i.config(bg='#c3c3c3')

    def indicate(self, lb, page, args):
        self.hide(args)
        lb.config(bg='#158aff')
        page()

    def home_page(self):
        home_frame = Frame(self.main_frame, width=400, height=400)
        home_frame.place(x=50, y=50)
        Label(home_frame, text='HOUSECLEANING', font=('Bold', 12), justify='left').place(x=10, y=10)
        Label(home_frame, text='ELECTRICITY SERVICE', font=('Bold', 12), justify='left').place(x=10, y=50)
        Button(home_frame, text='Choose', command=lambda: self.date_time()).place(x=350, y=10)
        Button(home_frame, text='Choose', command=lambda: self.date_time()).place(x=350, y=50)

    def history_page(self):
        history_frame = Frame(self.main_frame, width=400, height=400)
        history_frame.place(x=50, y=50)
        service_type = Label(history_frame, text='HOUSECLEANING (12.12.2021 - 9:00 a.m)', font=('Bold', 12), wraplength=350, justify='left')
        service_type.place(x=10, y=10)

    def about_page(self):
        about_frame = Frame(self.main_frame, width=400, height=400)
        about_frame.place(x=50, y=50)
        lb = Label(about_frame, text=ABOUT_TEXT, font=('Bold', 12), wraplength=350, justify='left')
        lb.place(x=20, y=20)

    def settings(self):
        settings_frame = Frame(self.main_frame, width=400, height=400)
        settings_frame.place(x=50, y=50)
        light = Button(settings_frame, text='Light mode', font=('Bold', 12), cursor='hand2', state='disabled', command=lambda: light_mode(light, dark))
        light.place(x=20, y=20)
        dark = Button(settings_frame, text='Dark mode', font=('Bold', 12), cursor='hand2', state='active', command=lambda: dark_mode(light, dark))
        dark.place(x=110, y=20)
        lb = Button(settings_frame, text='Log out', font=('Bold', 12), bg='blue', cursor='hand2', fg='white', command=lambda: quit())
        lb.place(x=20, y=100)

        def quit():
            self.main_frame.destroy()
            self.options_frame.destroy()
            auth = Authentification(window).sign_up_frame
            return auth

        def light_mode(light, dark):
            light.configure(state='disabled')
            dark.configure(state='active')
            self.options_frame.configure(bg='#c3c3c3')

        def dark_mode(light, dark):
            light.configure(state='active')
            dark.configure(state='disabled')
            self.options_frame.configure(bg='#36585c')

    def date_time(self):
        date = Frame(self.main_frame, width=400, height=400)
        date.place(x=50, y=50)
        cal = Calendar(date, selectmode='day',
                       year=2020, month=5,
                       day=22)
        cal.place(x=100, y=30)
        time_options = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM']

        # Create a Combobox widget
        time_combobox = ttk.Combobox(self.main_frame, values=time_options)
        time_combobox.set('9:00 AM')
        time_combobox.place(x=150, y=300)
        Button(self.main_frame, text='Order', padx=20, pady=10, fg='white', bg='blue', command=lambda: self.order(cal, time_combobox)).place(x=150, y=350)

    def order(self, cal, time):
        cal = cal.get_date()
        time = time.get()
        messagebox.showinfo("Sign In", f"Your request has been saved")
        print(cal, time)
        self.home_page()


if __name__ == '__main__':
    window = Tk()
    auth = Authentification(window)
    # admin = AdminPanel(window)
    # user = User(window)
    window.mainloop()
    client_socket.close()