#dictionary for storing the student data with the help of list objects.
#get refreshed when the program was executed again.
import os
os.chdir('C:/Users/srich/OneDrive/Desktop/')
os.getcwd()
d={'name_dict':[],'reg_dict':[],'branch_dict':[],'languages':[]}
#gui functions
from tkinter import *
def name_entry():
    print("Name: ",name.get())
def reg_entry():
    print("regd no: ",reg.get())
def branch():
    print("branch 1 - CSE ","branch 2 - IT")
    print("selected option: ",bvar.get())
def lang(event):
    global stld
    stld=lis.get(lis.curselection())
#submit button action
def printselection():
    #creating empty lists for storing the details of the students
    namesofst=[]
    regno=[]
    branches=[]
    languages=[]
    #extend method for insertion into list objects
    namesofst.append(name.get())
    regno.append(reg.get())
    if bvar.get()==1:
        branches.append('cse')
    else:
        branches.append('IT')
    languages.append(str(stld))
    #inserting into dictionary
    d['name_dict'].extend(namesofst[::-1])
    d['reg_dict'].extend(regno[::-1])
    d['branch_dict'].extend(branches[::-1])
    d['languages'].extend(languages[::-1])
    for x in d.items():
        print(x, end='  ')
    #converting created dictionary to csv file using pandas module
    import pandas as pd
    csvv=pd.DataFrame(d)
    print(d)
    csvv.to_csv('students.csv',index=False,mode='a')
    
#main window
a=Tk()
a.title("Student registration form")
a.geometry("800x450")
#name label
name_l=Label(a, text="name", fg="red",font=('arial',13))
#name entry
name=Entry(a,fg="black", bg="white")
name_l.place(x=0,y=0)
name.place(x=90,y=5)
#regno label
reg_l=Label(a, text="regd no", fg="red",font=('arial',13))
#regno entry
reg=Entry(a,fg="black", bg="white")
reg_l.place(x=0,y=30)
reg.place(x=90,y=35)
#submit button
b=Button(a,text="Submit", fg='red',bg='white',activebackground="green", command=printselection)
b.place(x=70,y=350)
#branch label
label_b=Label(a, text="BRANCH", fg="red",font=('arial',13))
label_b.place(x=0,y=60)
#radio buttons for branch selection
bvar=IntVar(value=0)
bv1=Radiobutton(a,text="CSE",value=1,variable=bvar)
bv2=Radiobutton(a,text="IT",value=2,variable=bvar)
bv1.place(x=30,y=90)
bv2.place(x=30,y=110)
#lang label
label_lang=Label(a, text="PROGRAMMING LANGUAGES KNOWN", fg="red",font=('arial',13))
label_lang.place(x=0,y=130)
#list box for languages selection
lis=Listbox(a)
for item in ['C','C++','Python']:
    lis.insert(END,item)
lis.bind("<<ListboxSelect>>",lang)
lis.place(x=20,y=160)
#running main loop
a.mainloop()
