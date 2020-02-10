import random
import tkinter as tk
from tkinter import messagebox
import sqlite3
import pyperclip

def dab3():
    conn=sqlite3.connect('p_book.db')
    cur=conn.cursor()

    cur.execute("delete from pass where user=?",(E6.get(),))
    messagebox.showinfo("Delete","Delete Successful")

    conn.commit()
    conn.close()

def dab2():
    conn = sqlite3.connect('p_book.db')
    cur = conn.cursor()
    user = E6.get()

    try:
        cur.execute("select purpose,password from pass where user=?",(user,))

        conn.commit()

        L7=tk.Label(r3,text= cur.fetchall(),font=('helvetica', 10, 'bold'))
        c3.create_window(150, 200, window=L7)

        button4 = tk.Button(r3, text='Delete Entry', width=10, height=1,command=dab3, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
        c3.create_window(150, 250, window=button4)
    except:
        messagebox.showerror("Unexpected Error Occurred!", "Username doesn't exist")

    conn.close()

def retrieve():
    global r3
    r3 = tk.Tk()
    r3.title('Password Generator')

    global c3
    c3 = tk.Canvas(r3, width=300, height=400)
    c3.pack()

    L6 = tk.Label(r3, text="User:")
    L6.config(font=('helvetica', 12, 'bold'))
    c3.create_window(80, 110, window=L6)

    global E6
    E6 = tk.Entry(r3)
    c3.create_window(170, 110, window=E6)

    button3 = tk.Button(r3, text='Retrieve Password', width=20, height=1,command=dab2, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
    c3.create_window(150, 150, window=button3)

    r3.mainloop()

def save():
    r2 = tk.Tk()
    r2.title('Password Generator')

    c2 = tk.Canvas(r2, width=300, height=300)
    c2.pack()

    L4 = tk.Label(r2, text="User:")
    L4.config(font=('helvetica', 12, 'bold'))
    c2.create_window(50, 80, window=L4)

    global E4
    E4 = tk.Entry(r2)
    c2.create_window(170, 80, window=E4)

    L5 = tk.Label(r2, text="Purpose:")
    L5.config(font=('helvetica', 12, 'bold'))
    c2.create_window(65, 130, window=L5)

    global E5
    E5 = tk.Entry(r2)
    c2.create_window(170, 130, window=E5)

    button2 = tk.Button(r2, text='Save Password', width=20, height=1, command=dab, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
    c2.create_window(150, 200, window=button2)

    r2.mainloop()

def dab():
    conn = sqlite3.connect('p_book.db')
    cur = conn.cursor()

    user = E4.get()
    purpose = E5.get()
    pw = password

    try:
        cur.execute("insert into pass values(?,?,?)", (user, purpose, pw))
        cur.execute("select * from pass")
        messagebox.showinfo("Save","Password saved successfully")
        conn.commit()
        print(cur.fetchall())
    except:
        messagebox.showerror("Unexpected Error Occurred!", "This username is already taken.\nPlease choose a different username.")

    conn.close()

def str(val):
    if val==0:
        return 97,123
    elif val==1:
        return 65,127
    elif val==2:
        return 41,127

def gen():
    beg,end= str(var.get())
    global password
    password = ''

    try:
        length = int(E1.get())
    except:
        messagebox.showerror("Unexpected Error Occurred","Enter a valid number")

    for i in range(length):
        password += chr(random.randrange(beg,end,1))

    L2=tk.Label(r, text="Your New Password:")
    L2.config(font=('helvetica', 10, 'bold'))
    c.create_window(200, 300, window=L2)

    L3 = tk.Label(r, text=password)
    L3.config(font=('helvetica', 12, 'bold'))
    c.create_window(200, 330, window=L3, width=1000)
    pyperclip.copy(password.strip())
    messagebox.showinfo("Password","Password copied to clipboard")

    button1 = tk.Button(r, text='Save', width=10, height=1, command=save, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
    c.create_window(200, 370, window=button1)

r = tk.Tk()
r.title('Password Generator')

c=tk.Canvas(r,width=400,height=500)
c.pack()

L1 = tk.Label(r, text = "Enter the length of your password: ")
L1.config(font=('helvetica', 12,'bold'))
c.create_window(200, 110, window=L1)

E1 = tk.Entry(r)
c.create_window(200, 150, window=E1)

var = tk.IntVar()
var.set(0)

R1 = tk.Radiobutton(r, text="Normal", variable=var, value=0)
c.create_window(200, 180, window=R1)

R2 = tk.Radiobutton(r, text="Strong", variable=var, value=1)
c.create_window(197, 200, window=R2)

R3 = tk.Radiobutton(r, text="Very Strong", variable=var, value=2)
c.create_window(210, 220, window=R3)

button = tk.Button(r, text='Generate Password', width=20,height=1, command=gen, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
c.create_window(200, 260, window=button)

button1 = tk.Button(r, text='Retrieve', width=10, height=1, command=retrieve, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
c.create_window(200, 400, window=button1)

r.mainloop()
