from tkinter import *
from tkinter import messagebox
import mysql.connector as mycon


#Creating Database

def CreateTable():                                               
        createDB="create database if not exists pwddb"
        use="use pwddb"
        createTable="create table if not exists pwds("\
                    "Username varchar(200) PRIMARY KEY," \
                    "Password varchar(200) NOT NULL)"
        

        conn = mycon.connect(host="localhost", user="root", password="dpsbn")     #Connecting to MySQL
        cur = conn.cursor()

        try:
            cur.execute(createDB)
            cur.execute(use)
            cur.execute(createTable)
            conn.commit()

        except:
            messagebox.showinfo("ERROR","Unable To Create Database")


def Login_Page(count=0):                 #Main Function of login page

    import HomeWindow as hw

    def signin():               #Function to signin to gain access 
        global count
        n=entry0.get()
        pwd=entry1.get()
        t=str((n,pwd))

        data=""

        with open("users.txt","a+") as fh:      #Setting default master password
            fh.seek(0)
            data=fh.read()
            if len(data)==0:
                fh.write(r"('admin', 'admin')")
                fh.seek(0)
                data=fh.read()
        
        if t in data:                                                    
            messagebox.showinfo("Message","Login Successful !")       #Loging in to home page
            CreateTable()
            window.destroy()
            hw.Home_Page()

        else:
            messagebox.showinfo("Message","Login Failed !")           #Error Message
            entry0.delete(0,END)
            entry1.delete(0,END)


    def signup():                          #Changing master password
        n=entry0.get()
        pwd=entry1.get()

        if len(n)==0 or len(pwd)==0:
            messagebox.showinfo("Error","Field Cannot Be Empty !")
        
        else:
            with open("users.txt","w") as fh:
                    fh.write(str((n,pwd))+'\n')
                    entry0.delete(0,END)
                    entry1.delete(0,END)
                    messagebox.showinfo("Success","Successfully Changed !")
    
    def nuf():
        messagebox.showinfo("Error","Login to change master password!")
        
    def decide():
        if count==1:          #Allowing change in master password only after login
            signup()
        else:
            nuf()


    window = Tk()                          #creating tkinter window

    window.geometry("600x400")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 400,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background3.png")   #Creating Background
    background = canvas.create_image(
        309.0, 210.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox03.png")     #Username entry field image
    entry0_bg = canvas.create_image(
        452.0, 163.0,
        image = entry0_img)

    entry0 = Entry(                                          #Username entry field
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry0.place(
        x = 338.0, y = 146,
        width = 228.0,
        height = 32)

    entry1_img = PhotoImage(file = f"img_textBox13.png")      #Master Password entry field image
    entry1_bg = canvas.create_image(
        452.0, 243.0,
        image = entry1_img)

    entry1 = Entry(                                           #Master Password entry field
        show='*',
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry1.place(
        x = 338.0, y = 226,
        width = 228.0,
        height = 32)

    img0 = PhotoImage(file = f"img03.png")         #signin button
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = signin,
        relief = "flat")

    b0.place(
        x = 373, y = 322,
        width = 66,
        height = 23)

    img1 = PhotoImage(file = f"img13.png")         #signup button
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = decide,
        relief = "flat")

    b1.place(
        x = 467, y = 322,
        width = 66,
        height = 23)

    window.resizable(False, False)
    window.mainloop()


if __name__=="__main__":
    CreateTable()
    Login_Page()