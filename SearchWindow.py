from tkinter import *
from tkinter import messagebox
import mysql.connector as mycon
import AddWindow as aw             #importing other pages
import main as lw
import HomeWindow as hw
import DeleteWindow as dw

 
def findRecord():                     #Finding a record
    entry1.delete(0,END)

    conn = mycon.connect(host="localhost", user="root", password="dpsbn", database="pwddb")
    cur = conn.cursor()

    Uname=entry0.get()

    try:
        getBooks = "select * from pwds where Username = '"+ Uname +"'"
        cur.execute(getBooks)
        dataRow = cur.fetchall()
        conn.commit()

        if len(dataRow)==0:                                           #Checking if user exists
            messagebox.showinfo("ERROR","Username doesn't exist")
        else:
            for i in dataRow:
                entry1.delete(0,END)
                entry1.insert(0,i[1])

    except:
        messagebox.showinfo("ERROR","Please Check input")



def Search_Page():
    global entry0,entry1,window

    def btn_clicked():              #if search button clicked
        pass
    
    def SwitchAddPage():            #if add button clicked
        window.destroy()
        aw.Add_Page()
    
    def SwitchLoginPage():          #if profile button clicked
        window.destroy()
        lw.Login_Page(1)
    
    def SwitchHomePage():           #if home button clicked
        window.destroy()
        hw.Home_Page()
    
    def SwitchDelPage():            #if delete button clicked
        window.destroy()
        dw.Delete_Page()


    window = Tk()                   #Creating tkinter window

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

    background_img = PhotoImage(file = f"background4.png")  #background image
    background = canvas.create_image(
        300.0, 200.0,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")   
    b0 = Button(                                        #Home Button
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchHomePage,
        relief = "flat")

    b0.place(
        x = 37, y = 68,
        width = 14,
        height = 13)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(                                        #Search button
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 38, y = 184,
        width = 12,
        height = 12)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(                                      #Profile button
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchLoginPage,
        relief = "flat")

    b2.place(
        x = 37, y = 335,
        width = 13,
        height = 11)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(                                      #Add button
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchAddPage,
        relief = "flat")

    b3.place(
        x = 38, y = 126,
        width = 12,
        height = 12)

    entry0_img = PhotoImage(file = f"img_textBox01.png")           #Username Entry
    entry0_bg = canvas.create_image(
        374.0, 131.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry0.place(
        x = 209.5, y = 120,
        width = 329.0,
        height = 25)
    
    entry1_img = PhotoImage(file = f"img_textBox01.png")     #Password Display
    entry1_bg = canvas.create_image(
        317.5, 217.5,
        image = entry0_img)

    entry1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry1.place(
        x = 158, y = 207,
        width = 329.0,
        height = 25)
    
    img4 = PhotoImage(file = f"img4.png")
    b4 = Button(                                       #Delete Button
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchDelPage,
        relief = "flat")

    b4.place(
        x = 38, y = 246,
        width = 12,
        height = 15)

    img5 = PhotoImage(file = f"img41.png")
    b5 = Button(                                        #Find Button
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = findRecord,
        relief = "flat")

    b5.place(
        x = 196, y = 156,
        width = 74,
        height = 24)

    window.resizable(False, False)
    window.mainloop()