import customtkinter as tk
import tkinter 
from tkinter import *
from tkinter import messagebox
import datetime

tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

root=tk.CTk()
root.geometry("1000x700")

x=0
a=0
n=0
t=[]
o=""
j=[0]
i=0
g=0
r=0
idk15=0
def p_val():
    global j
    global i
    j[i]=1
def l():
    global g
    global t
    global j
    global i
    global r
    g=0
    r=0
    o = int(check.get())
    f=open('dwe.txt','r')
    s=f.read()
    p=s.splitlines()
    f.close()
    for i in p:
        t.append(int(i))
    for i in range(len(t)-len(j)):
        j.append(0)
    for g in range(0,len(t)):
        r=r+1
        if(o==t[g]):
            i=t.index(o)
            if j[i]==0:
                p_val()
                buttonframe.pack()
                noti.pack_forget()
                reveal.pack_forget()
                btn20.pack_forget()
            else:
                messagebox.showerror(message="Already voted")
                check.delete(0,"end")
            break
        elif (r==len(t)):
            messagebox.showerror(message="could not be identified")
            check.delete(0,"end")
            break
def comm():
    now=datetime.datetime.now()
    data=open('data.txt','a')
    now=str(now)
    the_input=check.get()
    data.write(the_input+'   '+now+'\n')
    data.close()
def b():
    global x
    x=x+1
    buttonframe.pack_forget()
    noti.pack(pady=10)
    comm()
    check.delete(0, "end")



def c():
    global a
    a=a+1
    buttonframe.pack_forget()
    noti.pack(pady=10)
    comm()
    check.delete(0, "end")

def d():
    global n
    n=n+1
    buttonframe.pack_forget()
    noti.pack(pady=20)
    comm()
    check.delete(0,'end')
def term_data():
    read_file = open("data.txt", "r")
    data_read = read_file.read()
    cdt=datetime.datetime.today()
    date = str('%s/%s/%s' % (cdt.month, cdt.day, cdt.year))
    read_perm=open("permstorage.txt",'a')
    read_perm.write(f"{date} \n {data_read}")
    read_perm.close()
    read_file.close()
    read_file=open("data.txt",'w')
    read_file.write(" ")
    read_file.close()
    show()

def show():
  global x
  global a
  global n
  global results
  results = ""
  candidates=['BJP',"CONG",'AAP']
  new_list=[x,a,n]
  for i in range(3):
      percentage = round((new_list[i] / (a+x+n)) * 100, 2)
      results += f"{candidates[i]}: {new_list[i]} votes ({percentage}%)\n"
  if (x>a):
      if (x>n):
          messagebox.showinfo(title="RESULT", message=f"BJP WON \n {results}")
          exit()
  if (a>x):
      if (a>n):
          messagebox.showinfo(title="RESULT", message=f"Congress won \n {results}")
          exit()
  if(n>a):
      if(n>x):
          messagebox.showinfo(title="RESULT", message=f"AAP won \n {results}")
          exit()
  if n==a and n==x:
      messagebox.showinfo(title='RESULT',message=f'ALL 3 parties are tied \n {results} ')
      exit()
  if x==a and x>n:
      messagebox.showinfo(title='result',message=f'BJP and Congress are tied \n {results} ')
      exit()
  if a==n and x<a:
      messagebox.showinfo(title='result',message=f'AAP and Congress are tied \n {results}',font=("Arial",23))
      exit()
  if x==n and x>a:
      messagebox.showinfo(title='result',message=f'BJP and AAP are  tied \n {results}')
      exit()

def k():
    if(reveal.get().isdigit()==True):
        if(int(reveal.get())==456):
            buttonframe2.pack()
        else:
            messagebox.showinfo(message="incorrect")
            reveal.delete(0,'end')
    else:
        messagebox.showinfo(message="Incorrect")
        reveal.delete(0,'end')
def ball():
    text12.pack()
    butn_confirm.pack(padx=10,pady=10)
    buttonframe2.pack_forget()
    reveal.delete(0,'end')
    show_hide()

def store():
    checktrue=messagebox.askquestion(message="Do you want to store data to permananent text file and remove from temporary storage")
    if checktrue=='yes':
        term_data()
    else:
        show()
def addtolist():
    if (text12.get()).isdigit()==True:
        y = ''
        numbers = []
        reader = 0
        f = open('dwe.txt', 'r')
        file = f.read()
        lines = file.splitlines()
        f.close()
        for i in lines:
            numbers.append(int(i))
        reader = int(text12.get())
        if (numbers.count(reader) == 1):
            messagebox.showerror(message='already registered')
            text12.delete(0, 'end')
            text12.pack_forget()
            buttonframe2.pack_forget()
            butn_confirm.pack_forget()
        else:
            f = open("dwe.txt", 'a')
            y = y + '\n' + str(reader)
            f.write(y)
            messagebox.showinfo(message="Registration complete")
            text12.delete(0, 'end')
            text12.pack_forget()
            buttonframe2.pack_forget()
            butn_confirm.pack_forget()
    else:
        messagebox.showinfo(message="Enter integer values")
        text12.delete(0,'end')
        text12.pack_forget()
        butn_confirm.pack_forget()
def show_reveal():
    reveal.pack(pady=10)
    btn20.pack(pady=10)
def show_hide():
    reveal.pack_forget()
    btn20.pack_forget()

output=tk.CTkLabel(master=root,text="EVM",font=("Jetbrains Mono ExtraBold",80))
output.pack(padx=10,pady=20)

idk=tk.CTkButton(master=root,text="Voter id:",height=10,text_color='red',font=('Monotype Corsiva',30),fg_color='cyan')
idk.pack(padx=10,pady=10)
check=tk.CTkEntry(master=root,height=35,font=("Arial",20),width=400)
check.pack(padx=10,pady=10)

btn100=tk.CTkButton(master=root,text="Enter",command=l,font=('MV Boli',18))
btn100.pack(pady=20)

buttonframe = tk.CTkFrame(master=root)
buttonframe.columnconfigure(0, weight=1)

btn1=tk.CTkButton(master=buttonframe,text="BJP",font=("Ariel", 25),text_color='orange',command=b)
btn1.grid(row=0,column=0,sticky=tk.W+tk.E,pady=7)

btn2=tk.CTkButton(master=buttonframe,text="CONGRESS",font=("Ariel", 25),text_color='pink',command=c)
btn2.grid(row=8,column=0,sticky=tk.W+tk.E,pady=7)
btn3=tk.CTkButton(master=buttonframe,text="AAP",font=("Ariel", 25),text_color='white',command=d)
btn3.grid(row=18,column=0,sticky=tk.W+tk.E,pady=7)
buttonframe.pack_forget()
buttonframe2=tk.CTkFrame(master=root)
buttonframe2.columnconfigure(0,weight=1)
btn4=tk.CTkButton(master=buttonframe2,text="show result",font=("MV Boli", 18),command=store)
btn4.grid(row=0,column=0,sticky=tk.W+tk.E,pady=5)
btn5=tk.CTkButton(master=buttonframe2,text="add user",command=ball,font=("MV Boli", 18))
btn5.grid(row=1,column=0,sticky=tk.W+tk.E,pady=5)

buttonframe2.pack_forget()

text12=tk.CTkEntry(master=root,height=1,width=250,font=('ariel',18),placeholder_text="Enter the username here:")
text12.pack_forget()
butn_confirm=tk.CTkButton(master=root,text="Enter(note: only accepting integer usernames):",command=addtolist)
butn_confirm.pack_forget()

noti=tk.CTkButton(master=root,text="ADMINS LOGIN",font=('Bookman Old Style',20),text_color='cyan',command=show_reveal)
noti.pack(padx=10,pady=10)
reveal=tk.CTkEntry(master=root,height=1,width=230,placeholder_text="Enter the password here",show='*',font=('Ariel',20))
reveal.pack_forget()
btn20=tk.CTkButton(master=root,text="OK",font=("Ariel", 18),command=k)
btn20.pack_forget()
qrc=PhotoImage(file="QR.png")
Button(root,text="Tutorial",image=qrc,compound=BOTTOM).place(x=1450,y=850)

root.mainloop()
