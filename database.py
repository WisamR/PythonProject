
#==================================Import libaries=======================================
 
from Tkinter import *                   #For Gui
import sqlite3                          #For Database
import ttk as ttk                       #for GUI widgets
import tkMessageBox as tkMessageBox     #For Message Box

#==================================Import Windows=======================================
#The position and construction of the main page
root = Tk()                                         
root.title("Python: Simple CRUD Applition")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 550
x = (screen_width/2) - (width/2)   #Position of the main page
y = (screen_height/2) - (height/2) #Position of the main page
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


#==================================Define CRUD FUNCTIONS=======================================
#Creating and connecting the different command of the database

#open database connection
def Database():
    global conn, cursor
    conn = sqlite3.connect('pythontut.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname TEXT, lastname TEXT, gender TEXT, address TEXT, username TEXT, password TEXT)")
#FOR CREATING USER
def Create():

    #CHECKS IF ALL FIELD ARE SUPPLIED#
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or ADDRESS.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `member` (firstname, lastname, gender, address, username, password) VALUES(?, ?, ?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(ADDRESS.get()), str(USERNAME.get()), str(PASSWORD.get())))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        conn.commit()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        ADDRESS.set("")
        USERNAME.set("")
        PASSWORD.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Created a data!", fg="green")
#for updating values
def update():
    Database()
    if ID.get() =="":    #checks if id is not empty
        txt_result.config(text="Please Provide ID", fg="red")
    #Check all of the item are not empty
    elif  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or ADDRESS.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")

    #check Which one of the personal details to be updated
    if FIRSTNAME.get() != "":
        cursor.execute("UPDATE member SET firstname=?  WHERE mem_id = ?", (str(FIRSTNAME.get()),str(ID.get())))
        txt_result.config(text="Updated Firstname", fg="green")
    if LASTNAME.get()!= "":
        cursor.execute("UPDATE member SET lastname=?  WHERE mem_id = ?", (str(LASTNAME.get()),str(ID.get())))
        txt_result.config(text="Updated Lastname!", fg="green")
    if GENDER.get()!= "":
        cursor.execute("UPDATE member SET gender=?  WHERE mem_id = ?", (str(GENDER.get()),str(ID.get())))
        txt_result.config(text="Updated gender!", fg="green")
    if ADDRESS.get()!= "":
        cursor.execute("UPDATE member SET address=?  WHERE mem_id = ?", (str(ADDRESS.get()),str(ID.get())))
        txt_result.config(text="Updated address!", fg="green")
    if USERNAME.get()!= "":
        cursor.execute("UPDATE member SET username=?  WHERE mem_id = ?", (str(USERNAME.get()),str(ID.get())))
        txt_result.config(text="Updated username!", fg="green")
    if PASSWORD.get()!= "":
        cursor.execute("UPDATE member SET password=?  WHERE mem_id = ?", (str(PASSWORD.get()),str(ID.get())))
        txt_result.config(text="Updated passwords!", fg="green")
   

    # Saving our update
    conn.commit()
    cursor.close()
    conn.close()
    
### TO delete
def delete():
    Database()
    #Check if id is not empty
    if ID.get() =="":
        txt_result.config(text="Please Provide ID", fg="red")
    else:
        sql = "DELETE FROM member Where mem_id = ?"
        cursor.execute(sql,(str(ID.get()),))
        conn.commit()
        cursor.close()
        conn.close()
        txt_result.config(text="Deleted DATA!", fg="green")
        




#### READING DATA
def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0],data[1], data[2], data[3], data[4], data[5], data[6]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the data from database", fg="black")



##Creating the Exit Function

def Exit():
    result = tkMessageBox.askquestion('CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()



#==================================VARIABLES==========================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
ADDRESS = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()
ID = StringVar()
 
#==================================FRAME==============================================
# To create the frame of the main page
Top = Frame(root, width=900, height=50, bd=12, relief="raise") #fixing position of the frame
Top.pack(side=TOP)

Left = Frame(root, width=800, height=500, bd=18, relief="raise")    #fixing position of the frame
Left.pack(side=LEFT)

Right = Frame(root, width=600, height=500, bd=8, relief="raise")    #fixing position of the frame
Right.pack(side=RIGHT)

Forms = Frame(Left, width=800, height=700)  #fixing position of the left part where the fields
Forms.pack(side=TOP)

Buttons = Frame(Left, width=800, height=300, bd=8, relief="raise") #fixing position of the frame
Buttons.pack(side=BOTTOM)

RadioGroup = Frame(Forms)
Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('times new roman', 15)).pack(side=LEFT)
Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('times new roman', 15)).pack(side=LEFT)
 
#==================================LABEL WIDGET=======================================
# formatting the appearance of the main page including font type and the size of the font used. 
txt_title = Label(Top, width=900, font=(('times new roman', 22)), text = "Python: Simple CRUD Application, Final assignment")
txt_title.pack()

txt_firstname = Label(Forms, text="Firstname:", font=('times new roman', 15), bd=15)
txt_firstname.grid(row=0, stick="e")

txt_lastname = Label(Forms, text="Lastname:", font=('times new roman', 15), bd=15)
txt_lastname.grid(row=1, stick="e")

txt_gender = Label(Forms, text="Gender:", font=('times new roman', 15), bd=15)
txt_gender.grid(row=2, stick="e")

txt_address = Label(Forms, text="Address:", font=('times new roman', 15), bd=15)
txt_address.grid(row=3, stick="e")

txt_username = Label(Forms, text="Username:", font=('times new roman', 15), bd=15)
txt_username.grid(row=4, stick="e")

txt_password = Label(Forms, text="Password:", font=('times new roman', 15), bd=15)
txt_password.grid(row=5, stick="e")

txt_id = Label(Forms, text="Update or Delete ID", font=('times new roman', 15), bd=15)
txt_id.grid(row=6, stick="e")


txt_result = Label(Buttons)
txt_result.pack(side=TOP)
 
#==================================ENTRY WIDGET=======================================
iD= Entry(Forms, textvariable=ID, width=30)     #position and size of the entry field
iD.grid(row=6, column=1)

firstname = Entry(Forms, textvariable=FIRSTNAME, width=30)  #position and size of the entry field
firstname.grid(row=0, column=1)

lastname = Entry(Forms, textvariable=LASTNAME, width=30)  #position and size of the entry field
lastname.grid(row=1, column=1)

RadioGroup.grid(row=2, column=1)    #position and size of the entry field of "gender"

address = Entry(Forms, textvariable=ADDRESS, width=30)   #position and size of the entry field
address.grid(row=3, column=1)

username = Entry(Forms, textvariable=USERNAME, width=30)  #position and size of the entry field
username.grid(row=4, column=1)

password = Entry(Forms, textvariable=PASSWORD, show="*", width=30)  #position and size of the entry field
password.grid(row=5, column=1)
 
#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=Create)   #position and size of command "Create"
btn_create.pack(side=LEFT)

btn_read = Button(Buttons, width=10, text="Read", command=Read )        #position and size of command "Read"
btn_read.pack(side=LEFT)

btn_update = Button(Buttons, width=10, text="Update", command=update)   #position and size of command "Update"
btn_update.pack(side=LEFT)

btn_delete = Button(Buttons, width=10, text="Delete", command=delete)   #position and size of command "Delete"
btn_delete.pack(side=LEFT)

btn_exit = Button(Buttons, width=10, text="Exit", command=Exit) #position and size of command "Exit"
btn_exit.pack(side=LEFT)
 
#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=('ID',"Firstname", "Lastname", "Gender", "Address", "Username", "Password"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=150)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.pack()
#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
