'''
   add a way to stop infinite user loops
   add save and load functions
'''
import tkinter as tk,sys
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font
from io import StringIO

def outputting():
   sys.stdout = buffer = StringIO()
   userCodeInput=txtinput.get('1.0','end')
   try:
      exec(userCodeInput,globals())
   except KeyboardInterrupt:
      return
   except Exception as e:
      print(e)
   txtoutput.delete('1.0','end')
   txtoutput.insert('1.0',buffer.getvalue())

def orientation():
   if txtinput.pack_info()['side']=='left':
      txtinput.pack(side=tk.TOP)
   else:
      txtinput.pack(side=tk.LEFT)

window = tk.Tk()
window.title('PyCode')
toolbar, userIO= tk.Frame(window),tk.Frame(window)

txtinput,txtoutput = ScrolledText(userIO,background='white',foreground='black',width=60,height=20),ScrolledText(userIO,background='black',foreground='white',width=60,height=20)
font=Font(font=txtinput['font'])
tabWidth=font.measure(' ' * 3)
txtinput.config(tabs=tabWidth)
runbtn = tk.Button(toolbar,text='Run Code',command=lambda:outputting())
orientbtn=tk.Button(toolbar,text='Rotate',command=lambda:orientation())
txtinput.pack(side=tk.LEFT)
txtoutput.pack()
orientbtn.pack(side=tk.LEFT)
runbtn.pack(side=tk.RIGHT)

toolbar.pack()
userIO.pack()
window.mainloop()