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

def addF():
   def getFile():
      x=of()
      inpD.configure(state=NORMAL)
      inpD.delete(0,'end')
      inpD.insert(0,x)
      addfile.lift()
      inpD.configure(state=DISABLED)
   def checkLen():
      if len(inpD.get())>0 and len(inpF.get())>2:
         fm.files.createIt(f'{inpD.get()}/{inpF.get()}')
         addfile.destroy()
      else:print(FALSE)
   addfile=Toplevel()
   addfile.geometry('500x200')
   of= askdirectory
   addfile.title(f'{txt[0]}{txt1[0]}')
   lblI= Label(addfile,text='Use the form below to create a new file\n\n1st) First select the desired directory for which you want this new file to be created in\n\n2nd) Choose your new file\'s name, which must include it\'s file extention.\nExample: file.txt\n\n')
   lblD= Label(addfile,text='New File\'s Directory:')
   lblF= Label(addfile,text='New File\'s Name:')
   inpD= Entry(addfile,width=50,state=DISABLED)
   inpF= Entry(addfile,width=30)
   getD= Button(addfile,text='Browse',command=lambda:getFile())
   submit=Button(addfile,text='Submit',command=lambda:checkLen())
   lblI.grid(row=0,column=0,columnspan=4)
   lblD.grid(row=1,column=0)
   lblF.grid(row=2,column=0,sticky='e')
   inpD.grid(row=1,column=1,columnspan=2,pady=5,padx=5,sticky='w')
   inpF.grid(row=2,column=1,pady=5,padx=5,sticky='w')
   getD.grid(row=1,column=3)
   submit.grid(row=2,column=2,sticky='w')


def renameF():
   def getFile():
      x=of()
      inpD.configure(state=NORMAL)
      inpD.delete(0,'end')
      inpD.insert(0,x)
      addfile.lift()
      inpD.configure(state=DISABLED)
   def checkLen():
      if len(inpD.get())>0 and len(inpF.get())>2:
         fm.files.renameIt(f'{inpD.get()}',f'{inpF.get()}')
         addfile.destroy()
      else:print(FALSE)
   addfile=Toplevel()
   addfile.geometry('500x200')
   of= askopenfilename
   addfile.title(f'{txt[1]}{txt1[0]}')
   lblI= Label(addfile,text='Use the form below to rename a file\n\n1st) First select the desired file for which you want to rename\n\n2nd) Choose your file\'s new name, which must include it\'s file extention.\nExample: file.txt\n\n')
   lblD= Label(addfile,text='Old File\'s Directory:')
   lblF= Label(addfile,text='New File\'s Name:')
   inpD= Entry(addfile,width=50,state=DISABLED)
   inpF= Entry(addfile,width=30)
   getD= Button(addfile,text='Browse',command=lambda:getFile())
   submit=Button(addfile,text='Submit',command=lambda:checkLen())
   lblI.grid(row=0,column=0,columnspan=4)
   lblD.grid(row=1,column=0)
   lblF.grid(row=2,column=0,sticky='e')
   inpD.grid(row=1,column=1,columnspan=2,pady=5,padx=5,sticky='w')
   inpF.grid(row=2,column=1,pady=5,padx=5,sticky='w')
   getD.grid(row=1,column=3)
   submit.grid(row=2,column=2,sticky='w')

def moveF():print('3')

def deleteF():
   def getFile():
      x=of()
      inpD.configure(state=NORMAL)
      inpD.delete(0,'end')
      inpD.insert(0,x)
      addfile.lift()
      inpD.configure(state=DISABLED)
   def checkLen():
      if len(inpD.get())>0 :
         fm.files.deleteIt(f'{inpD.get()}')
         addfile.destroy()
      else:print(FALSE)
   addfile=Toplevel()
   addfile.geometry('500x200')
   of= askopenfilename
   addfile.title(f'{txt[3]}{txt1[0]}')
   lblI= Label(addfile,text='Use the form below to delete a file\n\n1st) First select the file that you desire to delete\n\n2nd) Press the delete button\n\n')
   lblD= Label(addfile,text='File\'s Directory:')
   inpD= Entry(addfile,width=50,state=DISABLED)
   getD= Button(addfile,text='Browse',command=lambda:getFile())
   submit=Button(addfile,text='Delete',command=lambda:checkLen())
   lblI.grid(row=0,column=0,columnspan=4)
   lblD.grid(row=1,column=0)
   inpD.grid(row=1,column=1,columnspan=2,pady=5,padx=5,sticky='w')
   getD.grid(row=1,column=3)
   submit.grid(row=2,column=2,sticky='w')

def addD():
   def getDir():
      x=of()
      inpD.configure(state=NORMAL)
      inpD.delete(0,'end')
      inpD.insert(0,x)
      addfolder.lift()
      inpD.configure(state=DISABLED)
   def checkLen():
      if len(inpD.get())>0 and len(inpF.get())>2:
         fm.folders.createIt(f'{inpD.get()}/{inpF.get()}')
         addfolder.destroy()
      else:print(FALSE)
   addfolder=Toplevel()
   addfolder.geometry('550x200')
   of= askdirectory
   addfolder.title(f'{txt[0]}{txt1[1]}')
   lblI= Label(addfolder,text='Use the form below to create a new folder\n\n1st) First select the desired/parent directory for which you want this new folder to be created in\n\n2nd) Choose your new folder\'s name which must include a minimum of 3 characters\n\n')
   lblD= Label(addfolder,text='New Folder\'s Parent Directory:')
   lblF= Label(addfolder,text='New Folder\'s Name:')
   inpD= Entry(addfolder,width=50,state=DISABLED)
   inpF= Entry(addfolder,width=30)
   getD= Button(addfolder,text='Browse',command=lambda:getDir())
   submit=Button(addfolder,text='Submit',command=lambda:checkLen())
   lblI.grid(row=0,column=0,columnspan=4)
   lblD.grid(row=1,column=0)
   lblF.grid(row=2,column=0,sticky='e')
   inpD.grid(row=1,column=1,columnspan=2,pady=5,padx=5,sticky='w')
   inpF.grid(row=2,column=1,pady=5,padx=5,sticky='w')
   getD.grid(row=1,column=3)
   submit.grid(row=2,column=2,sticky='w')

def renameD():
   def getFile():
      x=of()
      inpD.configure(state=NORMAL)
      inpD.delete(0,'end')
      inpD.insert(0,x)
      addfile.lift()
      inpD.configure(state=DISABLED)
   def checkLen():
      if len(inpD.get())>0 and len(inpF.get())>2:
         fm.folders.renameIt(f'{inpD.get()}',f'{inpF.get()}')
         addfile.destroy()
      else:print(FALSE)
   addfile=Toplevel()
   addfile.geometry('500x200')
   of= askdirectory
   addfile.title(f'{txt[1]}{txt1[1]}')
   lblI= Label(addfile,text='Use the form below to rename a folder\n\n1st) First select the desired folder for which you want to rename\n\n2nd) Choose your folder\'s new name\nExample: new_folder\n\n')
   lblD= Label(addfile,text='Old Folder\'s Directory:')
   lblF= Label(addfile,text='New Folder\'s Name:')
   inpD= Entry(addfile,width=50,state=DISABLED)
   inpF= Entry(addfile,width=30)
   getD= Button(addfile,text='Browse',command=lambda:getFile())
   submit=Button(addfile,text='Submit',command=lambda:checkLen())
   lblI.grid(row=0,column=0,columnspan=4)
   lblD.grid(row=1,column=0)
   lblF.grid(row=2,column=0,sticky='e')
   inpD.grid(row=1,column=1,columnspan=2,pady=5,padx=5,sticky='w')
   inpF.grid(row=2,column=1,pady=5,padx=5,sticky='w')
   getD.grid(row=1,column=3)
   submit.grid(row=2,column=2,sticky='w')

def moveD():print('3')
def deleteD():
   def getFile():
      x=of()
      inpD.configure(state=NORMAL)
      inpD.delete(0,'end')
      inpD.insert(0,x)
      addfile.lift()
      inpD.configure(state=DISABLED)
   def checkLen():
      if len(inpD.get())>0 :
         fm.folders.deleteIt(f'{inpD.get()}')
         addfile.destroy()
      else:print(FALSE)
   addfile=Toplevel()
   addfile.geometry('500x200')
   of= askdirectory
   addfile.title(f'{txt[3]}{txt1[1]}')
   lblI= Label(addfile,text='Use the form below to delete a folder\n\n1st) First select the folder that you desire to delete\n\n2nd) Press the delete button\n\n')
   lblD= Label(addfile,text='Folder\'s Directory:')
   inpD= Entry(addfile,width=50,state=DISABLED)
   getD= Button(addfile,text='Browse',command=lambda:getFile())
   submit=Button(addfile,text='Delete',command=lambda:checkLen())
   lblI.grid(row=0,column=0,columnspan=4)
   lblD.grid(row=1,column=0)
   inpD.grid(row=1,column=1,columnspan=2,pady=5,padx=5,sticky='w')
   getD.grid(row=1,column=3)
   submit.grid(row=2,column=2,sticky='w')

files=[addF,renameF,moveF,deleteF]
direc=[addD,renameD,moveD,deleteD]

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