from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from tkinter.ttk import Combobox
import openpyxl,xlrd
from openpyxl import Workbook
import pathlib

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

window = Tk()
window.title("Student Registration System | Ansuare school")
window.geometry("1250x700+210+100")
window.configure(bg = background)

file = pathlib.Path("Student_data.xlsx")
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet["A1"] = "Registration No."
    sheet["B1"] = "Name"
    sheet["C1"] = "Class"
    sheet["D1"] = "Gender"
    sheet["E1"] = "DOB"
    sheet["F1"] = "Date of Registration"
    sheet["G1"] = "Religion"
    sheet["H1"] = "Skill"
    sheet["I1"] = "Fathers's Name"
    sheet["J1"] = "Mother's Name"
    sheet["K1"] = "Father's Occupation"
    sheet["L1"] = "Mothers's Occupation"

    file.save("Student_data.xlsx")

#Exit window
def Exit():
    window.destroy()

def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetypes=(("JPG File","*.jpg"),("PNG","*.jpg"),("All files","*.txt")))
    img = (Image.open(filename))
    resized_image = img.resize((190,190))
    photo2 = ImageTk.PhotoImage(resized_image)
    lbl.config(image = photo2)
    lbl.image = photo2
#gender

def selection():
    value = radio.get()
    if value == 1:
        gender = "Male"
    else:
        gender = "Female"
#top frames

Label(window,text = "Email : dinnanischool@gmail.com",width= 10,height=3, bg = "#f0687c",anchor="e").pack(side = TOP,fill = X)
Label(window,text = "STUDENT'S REGISTRATION",width= 10,height=2,bg ="#c36464",fg = "#fff"   , font = "arial 20 bold").pack(side = TOP,fill = X)

#search box to update

Search = StringVar()
Entry(window,textvariable= Search,width=15,bd = 2,font="arial 20").place(x = 850, y = 68)
imageicon3 = PhotoImage( file = "search.png")
Srch = Button(window,text = "search",compound=LEFT,image=imageicon3,width=123,height=35, bg = "#68ddfa", font= "arial 13 bold",cursor="hand2")
Srch.place(x = 1090, y = 66)

imageicon4 = PhotoImage(file="update.png")
Update_button = Button(window,image=imageicon4, bg = "#c36464",cursor="hand2")
Update_button.place(x = 50, y = 50)


#Registration and Date
Label(window,text= "Registration No:",font= "area 13",fg = framebg, bg = background).place(x = 30, y = 150)
Label(window,text= "Date:",font= "area 13",fg = framebg, bg = background).place(x = 500, y = 150)

Registration = StringVar()
Date = StringVar()

reg_entry = Entry(window,textvariable= Registration, width= 15, font= "arial 10")
reg_entry.place(x = 160,y = 150)

#Registration No()

today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(window,textvariable = Date, width = 15,font = "arial 10")
date_entry.place(x = 550, y = 150)

Date.set(d1)

#Student details

obj = LabelFrame(window, text = "Student's Details", font =  20, bd = 2, width = 900 , bg = framebg, fg = framefg,height = 250,relief = GROOVE)
obj.place( x = 50, y = 200)

Label(obj,text = "Full name:", font= "arial 13", bg = framebg, fg = framefg).place(x = 30, y= 50)
Label(obj,text = "Date of birth:", font= "arial 13", bg = framebg, fg = framefg).place(x = 30, y= 100)
Label(obj,text = "Gender:", font= "arial 13", bg = framebg, fg = framefg).place(x = 30, y= 150)

Label(obj,text = "Class:", font= "arial 13", bg = framebg, fg = framefg).place(x = 500, y= 50)
Label(obj,text = "Religion:", font= "arial 13", bg = framebg, fg = framefg).place(x = 500, y= 100)
Label(obj,text = "Skills:", font= "arial 13", bg = framebg, fg = framefg).place(x = 500, y= 150)

Name = StringVar()
name_entry = Entry(obj,textvariable = Name , width= 20, font = "arial 10")
name_entry.place(x = 160, y = 50)

DOB = StringVar()
dob_entry = Entry(obj,textvariable = DOB , width= 20, font = "arial 10")
dob_entry.place(x = 160, y = 100)

radio = IntVar()
R1 = Radiobutton(obj,text = "Male",variable=radio,value = 1, bg = framebg,fg = framefg,command=selection)
R1.place(x = 150, y = 150)
R1 = Radiobutton(obj,text = "Female",variable=radio,value = 2, bg = framebg,fg = framefg,command=selection)
R1.place(x = 200, y = 150)

Religion = StringVar()
religion_entry = Entry(obj,textvariable = Religion , width= 20, font = "arial 10")
religion_entry.place(x = 630, y = 100)

Skill= StringVar()
skill_entry = Entry(obj,textvariable = Skill , width= 20, font = "arial 10")
skill_entry.place(x = 630, y = 150)

Class = Combobox(obj,values = ["1","2","3","4","5","6","7","8","9","10","11","12"],font="Roboto 10",width=17,state= "r")
Class.place(x = 630, y = 50)
Class.set("Select class")



#Parents details

obj2 = LabelFrame(window, text="Parent's Details", font =20, bd = 2, width = 900, bg = framebg, fg = framefg,height = 220,relief = GROOVE)
obj2.place( x = 50, y = 470)

Label(obj2,text = "Father's name:", font= "arial 13", bg = framebg, fg = framefg).place(x=30, y=50)
Label(obj2,text = "Occupation:", font= "arial 13", bg = framebg, fg = framefg).place(x=30, y=100)

F_name = StringVar()
f_entry = Entry(obj2,textvariable = F_name, width= 20, font = "arial 10")
f_entry.place(x = 160, y = 50)

Father_Occupation = StringVar()
FO_entry = Entry(obj2,textvariable = Father_Occupation , width= 20, font = "arial 10")
FO_entry.place(x = 160, y = 100)

Label(obj2,text = "Mother's name:", font= "arial 13", bg = framebg, fg = framefg).place(x = 500, y= 50)
Label(obj2,text = "Occupation:", font= "arial 13", bg = framebg, fg = framefg).place(x = 500, y= 100)

M_name = StringVar()
m_entry = Entry(obj2,textvariable = M_name, width= 20, font = "arial 10")
m_entry.place(x = 630, y = 50)

Mother_Occupation = StringVar()
MO_entry = Entry(obj2,textvariable = Mother_Occupation , width= 20, font = "arial 10")
MO_entry.place(x = 630, y = 100)

#image
f = Frame(window,bd =3 ,bg = "black",width=200,height=200,relief = GROOVE)
f.place(x= 1000, y= 150)

img = PhotoImage(file = "upload.png")
lbl = Label(f,bg = "black",image= img)
lbl.place( x = 0, y = 0)

#Button

Button(window, text = "Upload", width=19, height = 2, font = "arial 12 bold", bg="lightblue",command=showimage,cursor="hand2").place(x = 1000, y = 370)
saveButton = Button(window, text = "Save", width=19, height = 2, font = "arial 12 bold", bg="lightgreen",cursor="hand2")
saveButton.place(x = 1000, y = 450)
Button(window, text = "Reset", width=19, height = 2, font = "arial 12 bold", bg="lightpink",cursor="hand2").place(x = 1000, y = 530)
Button(window, text = "Exit", width=19, height = 2, font = "arial 12 bold", bg="grey",command = Exit,cursor="hand2").place(x = 1000, y = 610)




window.mainloop()

