import configparser
import tkinter as tk


class DB_setup(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('250x150+550+350')
        self.title('DB CONFIG INFO')
        self.resizable(0, 0)
        
        config = configparser.ConfigParser()
        config.read('db_config.ini')
        
        
        # label 1
        label1 = tk.Label(self, text='DB login:')
        label1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        
        # label 2
        label2 = tk.Label(self, text=config['DB_CONFIG']['DB_USER'])
        label2.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        # label 3
        label3 = tk.Label(self, text='DB Password:')
        label3.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        
        # label 4
        label4 = tk.Label(self, text=config['DB_CONFIG']['DB_PASSWORD'])
        label4.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        
        # label 5
        label5 = tk.Label(self, text='DB Server:')
        label5.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        
        # label 6
        label6 = tk.Label(self, text=config['DB_CONFIG']['DB_SERVER'])
        label6.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        
        # button Start
        OK_button = tk.Button(self, text="OK", command=lambda:(quit()))
        OK_button.grid(column=1, row=12, sticky=tk.S, padx=10, pady=10)


if __name__ == "__main__":
    app = DB_setup()
    app.mainloop()  
