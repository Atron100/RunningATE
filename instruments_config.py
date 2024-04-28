import configparser
import tkinter as tk


class Instruments_Form(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('250x350+550+350')
        self.title('DB CONFIG INFO')
        self.resizable(0, 0)
        
        config = configparser.ConfigParser()
        config.read('instruments_config.ini')
        
        
        # label 1
        label1 = tk.Label(self, text='RELAY COM:')
        label1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
        
        # label 2
        label2 = tk.Label(self, text=config['RELAY']['COM'])
        label2.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        
        spacer1 = tk.Label(self, text="")
        spacer1.grid(row=1, column=0)
        # label 3
        label3 = tk.Label(self, text='ANALYZER IP:')
        label3.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
        
        # label 4
        label4 = tk.Label(self, text=config['ANALYZER']['IP'])
        label4.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # label 5
        label5 = tk.Label(self, text='ANALYZER COM:')
        label5.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
        
        # label 6
        label6 = tk.Label(self, text=config['ANALYZER']['COM'])
        label6.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
        spacer2 = tk.Label(self, text="")
        spacer2.grid(row=4, column=0)

        # label 7
        label7 = tk.Label(self, text='SCANNER 1:')
        label7.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)
        
        # label 8
        label8 = tk.Label(self, text=config['SCANNER']['UUT1'])
        label8.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        # label 9
        label9 = tk.Label(self, text='SCANNER 2:')
        label9.grid(column=0, row=6, sticky=tk.E, padx=5, pady=5)
        
        # label 10
        label10 = tk.Label(self, text=config['SCANNER']['UUT2'])
        label10.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
        # label 11
        label11 = tk.Label(self, text='SCANNER 3:')
        label11.grid(column=0, row=7, sticky=tk.E, padx=5, pady=5)
        
        # label 12
        label12 = tk.Label(self, text=config['SCANNER']['UUT3'])
        label12.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
        # label 13
        label13 = tk.Label(self, text='SCANNER 4:')
        label13.grid(column=0, row=8, sticky=tk.E, padx=5, pady=5)
        
        # label 14
        label14 = tk.Label(self, text=config['SCANNER']['UUT4'])
        label14.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
        # label 15
        label15 = tk.Label(self, text='SCANNER 5:')
        label15.grid(column=0, row=9, sticky=tk.E, padx=5, pady=5)
        
        # label 16
        label16 = tk.Label(self, text=config['SCANNER']['UUT5'])
        label16.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)

        
        
        # button Start
        OK_button = tk.Button(self, text="OK", command=lambda:(quit()))
        OK_button.grid(column=1, row=12, sticky=tk.S, padx=10, pady=10)


if __name__ == "__main__":
    app = Instruments_Form()
    app.mainloop()  