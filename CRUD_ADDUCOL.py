from tkinter import *
from tkinter import ttk
import tkinter.messagebox

employee = []


class Employees:
    def __init__(self, name, department, position, number):
        self.name = name
        self.sports = department
        self.position = position
        self.jerseynumber = number

    def getName(self):
        return self.name
    def getSports(self):
        return self.department
    def getPosition(self):
        return self.position
    def getJerseynumber(self):
        return self.number


def add():
    global employee
    MsgBox = tkinter.messagebox.askquestion ('Confirmation','Are you sure you want to add this item?',icon = 'warning')
    if MsgBox == 'yes':
        emp = Employees(textfield1.get(), textfield2.get(), textfield3.get(), textfield4.get())
        employee.append(emp)
        tview.insert('', 'end', text='tree', values=(textfield1.get(), textfield2.get(), textfield3.get(), textfield4.get()))

        
        items = (textfield4.get())
        if (items.isdigit()):
            textfield1.delete(0, 'end')
            textfield2.delete(0, 'end')
            textfield3.delete(0, 'end')
            textfield4.delete(0, 'end')
            return True
        else:
            error = "Wrong data type entered."
            tkinter.messagebox.showinfo("Warning", error)
            textfield1.delete(0, 'end')
            textfield2.delete(0, 'end')
            textfield3.delete(0, 'end')
            textfield4.delete(0, 'end')
            return False


    else:
        pass


def update():
    global Employees
    MsgBox = tkinter.messagebox.askquestion ('Confirmation','Are you sure you want to update this item?',icon = 'warning')
    if MsgBox == 'yes':
       selected_item = tview.selection()[0]
       tview.item(selected_item, values=(textfield1.get(), textfield2.get(), textfield3.get(), textfield4.get()))    

       textfield1.delete(0, 'end')
       textfield2.delete(0, 'end')
       textfield3.delete(0, 'end')
       textfield4.delete(0, 'end')
    else:
        pass

def delete():
    global employee
    MsgBox = tkinter.messagebox.askquestion ('Confirmation','Are you sure you want to delete this item?',icon = 'warning')
    if MsgBox == 'yes':
       selected_item = tview.selection()[0]
       tview.delete(selected_item)
    else:
        pass

def close():
    MsgBox = tkinter.messagebox.askquestion ('Exit Application','Are you sure you want to exit the program?',icon = 'warning')
    if MsgBox == 'yes':
       form.destroy()
    else:
        tkinter.messagebox.showinfo('Return','You will now be back on the Athletes Information')


def getSelection(event):
    global name_text
    global department_text
    global position_text
    global number_text

    selected_item = tview.selection()
    select = tview.item(selected_item,'values')

    name_text.set(select[0])
    department_text.set(select[1])
    position_text.set(select[2])
    number_text.set(select[3])



def validate(number):
    if number.isdigit():
        return True
    elif number is "":
        return True
    else:
        return False

form = Tk()
form.title("Employee's Account")
label = Label(form, text="Employee's Account", font=12)
label.grid(row=0, column=1)
label.config(font=("OCR A EXTENDED", 20, "bold"), fg='black', bg="white")

name_text=StringVar()
department_text=StringVar()
position_text = StringVar()
number_text = StringVar()

labelname = Label(form, text="Name:")
labelname.grid(row=2, column=0)

labelname = Label(form, text="Department:")
labelname.grid(row=3, column=0)

labelname = Label(form, text="Position:")
labelname.grid(row=2, column=2)

labelname = Label(form, text="Number:")
labelname.grid(row=3, column=2)

textfield1 = Entry(form, relief = FLAT, textvariable=name_text)
textfield1.grid(row=2, column=1)

textfield2 = Entry(form, relief = FLAT, textvariable=department_text)
textfield2.grid(row=3, column=1)

textfield3 = Entry(form, relief = FLAT, textvariable=position_text)
textfield3.grid(row=2, column=3)

textfield4 = Entry(form, relief = FLAT, textvariable=number_text)
textfield4.grid(row=3, column=3)

val = form.register(validate)
textfield4.config(validate="key",validatecommand=(val, '%P'))

button1 = Button(form, text="Add", command=add)
button1.grid(row=4, column=0, padx=3, pady=3 )
button2 = Button(form, text="Update",command=update)
button2.grid(row=4, column=1, padx=3, pady=3)
button3 = Button(form, text="Delete", command=delete)
button3.grid(row=4, column=2, padx=3, pady=3)
button4 = Button(form, text="Exit", command=close)
button4.grid(row=4, column=3, padx=3, pady=3)

tview = ttk.Treeview(form, column=("Name", "Department", "Position", "number"), show="headings")
tview.heading('#1', text='NAME')
tview.heading('#2', text='DEPARTMENT')
tview.heading('#3', text='POSITION')
tview.heading('#4', text='NUMBER')
tview.bind('<ButtonRelease-1>',getSelection)
tview.grid(row=5,column=0,columnspan=5)

