
import tkinter as tk


class Login_Form(tk.Tk):
    def __init__(self):
        super().__init__()       

        self.geometry('300x120+550+350')
        self.title('LOGIN FORM')
        self.resizable(0, 0)

        self.username = ""
        self.password = ""

        usr = tk.StringVar
        passw = tk.StringVar

        # username
        label1 = tk.Label(self, text="Username:")
        label1.grid(row=0, column=0, sticky=tk.W)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)
        self.username_entry.bind("<Return>", self.handle_username_entry)
        self.username_entry.focus()

        # Password Entry
        label2 = tk.Label(self, text="Password:")
        label2.grid(row=1, column=0, sticky=tk.W)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)
        self.password_entry.bind("<Return>", self.handle_password_entry)      
                 

        # button Start
        self.OK_button = tk.Button(self, text="OK", command=lambda:(quit()))
        self.OK_button.grid(column=1, row=12, sticky=tk.W, padx=10, pady=10)

        # button Start
        self.Cancel_button = tk.Button(self, text="Cancel", command=lambda:(quit()))
        self.Cancel_button.grid(column=1, row=12, sticky=tk.E, padx=10, pady=10)
        

    def handle_username_entry(self, event):
        self.username = self.username_entry.get()
        self.usr = self.username
        self.password_entry.focus_set()

    def handle_password_entry(self, event):
        self.password = self.password_entry.get()
        self.passw = self.password
        self.OK_button.focus_set()  
        self.login()
        

    def login(self):
        # You can put your login logic here
        # For simplicity, let's just print the username and password
        print("Username:", self.username)
        print("Password:", self.password) 
        print("Username:", self.usr)
        print("Username:", self.passw)

        

if __name__ == "__main__":
    app = Login_Form()
    app.mainloop()  