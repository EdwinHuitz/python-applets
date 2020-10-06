from tkinter import *
from tkinter.filedialog import *
import file_manager as fm

window = Tk()
window.geometry('410x300')
window.title('File Manager')

lbl = Label(text='Use this program to manage your files all in one place!')
frL = Frame(window)
frR = Frame(window)

lbl.pack()
frL.pack(side=LEFT,padx=5,pady=10)
frR.pack(side=RIGHT,padx=5,pady=10)

txt = ['Create a New','Rename an Existing','Move an Existing','Delete an Existing']
txt1 = [' File',' Directory']

def f1():
   def getFile():
      x=of()
      inpD.configure(state=NORMAL)
      inpD.delete(0,'end')
      inpD.insert(0,x)
      addfile.lift()
      inpD.configure(state=DISABLED)
   def checkl():
      if len(inpD.get())>0 and len(inpF.get())>2:
         fm.files.createIt(f'{inpD.get()}/{inpF.get()}')
         addfile.destroy()
      else:print(FALSE)
   addfile=Toplevel()
   addfile.geometry('500x200')
   of= askdirectory
   addfile.title(f'{txt[0]}{txt1[0]}')
   lbI= Label(addfile,text='Use the form below to create a new file\n\n1st) First select the desired directory for which you want this file to be created in\n2nd) Choose your new file\'s name, which must include it\'s file extention.\nExample: file.txt')
   lbD= Label(addfile,text='New File\'s Directory:')
   lbF= Label(addfile,text='New File\'s Name:')
   inpD= Entry(addfile,width=50,state=DISABLED)
   inpF= Entry(addfile,width=30)
   getD= Button(addfile,text='Browse',command=lambda:getFile())
   submit=Button(addfile,text='Submit',command=lambda:checkl())#print(f'{inpD.get()}/{inpF.get()}'))
   lbI.grid(row=0,column=0,columnspan=4)
   lbD.grid(row=1,column=0)
   lbF.grid(row=2,column=0,sticky='e')
   inpD.grid(row=1,column=1,columnspan=2,pady=5,padx=5,sticky='w')
   inpF.grid(row=2,column=1,pady=5,padx=5,sticky='w')
   getD.grid(row=1,column=3)
   submit.grid(row=2,column=2,sticky='w')

def f2():print('2')
def f3():print('3')
def f4():print('4')

def d1():print('1')
def d2():print('2')
def d3():print('3')
def d4():print('4')

files=[f1,f2,f3,f4]
direc=[d1,d2,d3,d4]

i=0
while i < 4:
   btnL=Button(frL)
   btnL.configure(text=f'{txt[i]}{txt1[0]}',width=25,height=3,command=lambda num=f'{i}':files[int(num)]())
   btnL.grid(row=i,column=0)
   btnR=Button(frR)
   btnR.configure(text=f'{txt[i]}{txt1[1]}',width=25,height=3,command=lambda num=f'{i}':direc[int(num)]())
   btnR.grid(row=i,column=0)
   i+=1

window.mainloop()