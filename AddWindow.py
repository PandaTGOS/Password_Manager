from tkinter import *
from tkinter import messagebox
import mysql.connector as mycon
import SearchWindow as sw         #importing other pages
import main as lw
import HomeWindow as hw
import DeleteWindow as dw
import random


def AddRecord():         #Executing sql commands to add a new record

    conn = mycon.connect(host="localhost", user="root", password="dpsbn", database="pwddb")
    cur = conn.cursor()
    
    uname = entry0.get()
    password = entry1.get()

    if uname=='' or password=='':
        messagebox.showinfo("ERROR","No entry given")
    
    else:
        insertBooks = "insert into pwds values('"+uname+"','"+password+"')"

        try:
            cur.execute(insertBooks)
            conn.commit()

            messagebox.showinfo('SUCCESS',"Record Added Successfully")
        except:
            messagebox.showinfo("ERROR","Unable To Add Record")
    
    entry0.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)
    


def generate():       #Function to generate a strong password

    try:
        lc=[]
        password=''                    #Generated Rassword
        n = int(entry2.get())          #Taking length of password as an entry

        if n<6 or n>12:                #Restricting password length
            messagebox.showinfo("INVALID INPUT","Enter length between 6 and 12 only")
        else:
            for i in range(n):
                if i%2==0:
                    lc.append(str(random.randint(0,9)))
                else:
                    r = random.choice([(33,47),(58,126)])
                    lc.append(chr(random.randint(*r)))
                
            random.shuffle(lc)      #Shuffling the letters
            for i in lc:
                password+=i
                    
            
            entry1.delete(0,END)
            entry1.insert(0,password)         #Displays ramdomly generated password
    
    except:
        messagebox.showinfo("ERROR","Check Input")




def Add_Page():                                   #Main function of Add Window
    global entry0,entry1,entry2

    #SideBar Buttons
    def btn_clicked():         #if add button clicked
        pass
    
    def SwitchLoginPage():     #if profile button clicked
        window.destroy()
        lw.Login_Page(1)
    
    def SwitchSearchPage():    #if search button clicked
        window.destroy()
        sw.Search_Page()
    
    def SwitchHomePage():      #if home button clicked
        window.destroy()
        hw.Home_Page()
    
    def SwitchDelPage():       #if delete button clicked
        window.destroy()
        dw.Delete_Page()


    window = Tk()                                #Creating tkinter window

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

    background_img = PhotoImage(file = f"background2.png")   #background image
    background = canvas.create_image(
        300.0, 200.0,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")     #Home Button
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = SwitchHomePage,
        relief = "flat")

    b0.place(
        x = 37, y = 68,
        width = 14,
        height = 13)

    img1 = PhotoImage(file = f"img1.png")     #Search Button
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

    img2 = PhotoImage(file = f"img2.png")     #Profile Button
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
        command = btn_clicked,
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

    entry0_img = PhotoImage(file = f"img_textBox02.png")        
    entry0_bg = canvas.create_image(
        402.0, 156,
        image = entry0_img)

    entry0 = Entry(                        #Username Entry
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)         

    entry0.place(
        x = 256.5, y = 142.5,
        width = 291.0,
        height = 25)

    entry1_img = PhotoImage(file = f"img_textBox12.png")
    entry1_bg = canvas.create_image(
        402.0, 203,
        image = entry1_img)

    entry1 = Entry(                          #Password Entry
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry1.place(
        x = 256.5, y = 191,
        width = 291.0,
        height = 25)
    
    entry2_img = PhotoImage(file = f"img_textBoxLen.png")
    entry2_bg = canvas.create_image(
        416.0, 250.5,
        image = entry2_img)

    entry2 = Entry(                            #Generated pwd Length Entry
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    entry2.place(
        x = 331.5, y = 237.5,
        width = 169.0,
        height = 25)


    img6 = PhotoImage(file = f"img42.png")
    b6 = Button(                                           #Add Button
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = AddRecord,
        relief = "flat")

    b6.place(
        x = 461, y = 295,
        width = 74,
        height = 24)

    img5 = PhotoImage(file = f"img52.png")       #Generate button
    b5 = Button(
       image = img5,
       borderwidth = 0,
       highlightthickness = 0,
       command = generate,
       relief = "flat")

    b5.place(
        x = 243, y = 295,
        width = 189,
        height = 24)

    window.resizable(False, False)
    window.mainloop()