from tkinter import *
import tkinter.messagebox
import sqlite3

connect = sqlite3.connect('userdata.db')
cursor = connect.cursor()
class buttonApplication():
    def __init__(self,master):
        self.master = master
    
        self.frame = Frame(master, width=320, height=300)
        self.frame.pack_propagate(0)
        self.frame.pack()

        self.username_label = Label(self.frame, text='Username: ', fg='black', font='arial')
        self.username_label.place(x=64, y=35)

        self.password_label = Label(self.frame, text='Password', fg='black', font='arial')
        self.password_label.place(x=64, y=108)

        self.username_ent = Entry(self.frame, width=30)
        self.username_ent.place(x=66, y=60)

        self.password_ent = Entry(self.frame, width=30)
        self.password_ent.place(x=66, y=130)

        self.button = Button(self.frame, text="login", command = self.checkUserdata)
        self.button.place(x=140, y=200)

    def checkUserdata(self):
        self.data_username = self.username.get()
        self.data_pass = self.password.get()
        sql = "SELECT * FROM userData WHERE username = ? AND password = ?"
        cursor.execute(sql, [(self.data_username),(self.data_pass)])
        self.result = cursor.fetchall()
        
        if self.result:
            tkinter.messagebox.showinfo('message',"login successfully !")
        else:
            tkinter.messagebox.showinfo('message',"login unsuccessful !")



root = Tk()
root.title('comparison app')
ba = buttonApplication(root)
root.mainloop()
