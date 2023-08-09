from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mycon
import main as lw                    #importing other pages
import SearchWindow as sw
import AddWindow as aw
import DeleteWindow as dw


def SeeRecords():             #Accesses records and Shows Table

    conn = mycon.connect(host="localhost", user="root", password="dpsbn", database="pwddb")
    cur = conn.cursor()

    try:
        getBooks = "select * from pwds order by Username"
        cur.execute(getBooks)
        dataRow = cur.fetchall()
        y = 0.25
        for i in dataRow:
            tree.insert("",END, values=i)

    except:
        messagebox.showinfo("ERROR", "Unable To Fetch Data")


 
def Home_Page():                        #Main Function of the Home Page
    global tree,window

    #SideBar Buttons
    def btn_clicked():             #if home button clicked
        pass
    
    def SwitchLoginPage():         #if profile button clicked
        window.destroy()
        lw.Login_Page(1)
    
    def SwitchSearchPage():        #if search button clicked
        window.destroy()
        sw.Search_Page()
    
    def SwitchAddPage():           #if add button clicked
        window.destroy()
        aw.Add_Page()
    
    def SwitchDelPage():           #if delete button clicked
        window.destroy()
        dw.Delete_Page()


    window = Tk()                     #Creating tkinter window

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

    background_img = PhotoImage(file = f"background1.png")    #Adding Background
    background = canvas.create_image(
        300.0, 200.0,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")       #Home Button
    b0 = Button( 
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 37, y = 68,
        width = 14,
        height = 13)

    img1 = PhotoImage(file = f"img1.png")       #Search Button
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchSearchPage,
        relief = "flat")

    b1.place(
        x = 38, y = 184,
        width = 12,
        height = 12)

    img2 = PhotoImage(file = f"img2.png")      #Profile Button
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchLoginPage,
        relief = "flat")

    b2.place(
        x = 37, y = 335,
        width = 13,
        height = 11)

    img3 = PhotoImage(file = f"img3.png")      #Add Button
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchAddPage,
        relief = "flat")

    b3.place(
        x = 38, y = 126,
        width = 12,
        height = 12)
    
    img4 = PhotoImage(file = f"img4.png")       #Delete Button
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchDelPage,
        relief = "flat")

    b4.place(
        x = 38, y = 246,
        width = 12,
        height = 15)

    
    #DISPLAYING ALL RECORDS - TreeView

    tree = ttk.Treeview(window, column=("c1", "c2"), show='headings')
    tree.column("#1", width=100, anchor=CENTER)
    tree.heading("#1", text="USERNAME")

    tree.column("#2", width=100, anchor=CENTER)
    tree.heading("#2", text="PASSWORD")

    tree.place(relx=0.165, rely=0.28, relwidth=0.78, relheight=0.6)


    SeeRecords()    #Accessing records

    window.resizable(False, False)
    window.mainloop()