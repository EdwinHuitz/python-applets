import calc
from tkinter import *


window = Tk()
label = Label(text='0')
fr0,fr1,fr2,fr3,frL,frR = Frame(window),Frame(window),Frame(window),Frame(window),Frame(window),Frame(window)
label.pack()
frL.pack(side=LEFT)
frR.pack(side=RIGHT)
fr3.pack()
fr2.pack()
fr1.pack()
fr0.pack()
bottombtn = [Button(fr0, text='C',command=lambda a='C':doit(a)),Button(fr0,text='0',command=lambda a='0':doit(a)),Button(fr0,text='.',command=lambda a='.':doit(a))]
sidebtn = [Button(frL, text='+',command=lambda a='+':doit(a)),Button(frL,text='-',command=lambda a='-':doit(a)),Button(frL,text='=',command=lambda a='=':doit(a)),Button(frR, text='*',command=lambda a='*':doit(a)),Button(frR,text='/',command=lambda a='/':doit(a)),Button(frR,text='%',command=lambda a='%':doit(a))]
inp,inp1,op = '','',''
def doit(num):
   global inp,inp1,op
   #clear
   if num == 'C':
      inp,inp1,op='','',''
      print(num+' and '+inp+' and '+inp1+' and '+op)
      label.configure(text='0')
   #decimal
   elif num == '.' and inp=='':
      inp+='0.'
      print(num+' and '+inp)
      label.configure(text=inp)
   elif num == '.':
      if inp.find('.')<0:
         inp+='.'
         print(num+' and '+inp)
         label.configure(text=inp)
   #add
   elif num == '+':
      if op == '':
         op='+'
         inp1=inp
         label.configure(text=inp1+op)
         inp=''
      else:
         inp1 = calc.math(inp1,op,inp)
         op='+'
         inp = ''
         label.configure(text=inp1+op)
   #subtract
   elif num == '-':
      if op == '':
         inp1=inp
         op='-'
         label.configure(text=inp1+op)
         inp=''
      else:
         inp1 = calc.math(inp1,op,inp)
         op='-'
         inp = ''
         label.configure(text=inp1+op)
   #multiply
   elif num == '*':
      if op == '':
         inp1=inp
         op='*'
         label.configure(text=inp1+op)
         inp=''
      else:
         inp1 = calc.math(inp1,op,inp)
         op='*'
         inp = ''
         label.configure(text=inp1+op)
   #divide
   elif num == '/':
      if op == '':
         inp1=inp
         op='/'
         label.configure(text=inp1+op)
         inp=''
      else:
         inp1 = calc.math(inp1,op,inp)
         op='/'
         inp = ''
         label.configure(text=inp1+op)
   #sum
   elif num == '=':
      if op == '':
         label.configure(text=inp)
      else:
         inp = calc.math(inp1,op,inp)
         label.configure(text=inp)
         op=''
         inp1=''
   elif num.isnumeric():
      inp+=num
      print(num+' and '+inp)
      label.configure(text=inp1+op+inp)

i=0
tr=0
td=0
while i < 9:
   btns = [Button(fr1),Button(fr2),Button(fr3)]
   btns[tr].configure(command=lambda a=f'{i+1}':doit(a),height=4,width=6)
   if i<3:
      sidebtn[i].configure(height=4,width=6)
      sidebtn[i].pack()
      bottombtn[i].configure(height=4,width=6)
      bottombtn[i].pack(side=LEFT)
   elif i>2 and i<6:
      sidebtn[i].configure(height=4,width=6)
      sidebtn[i].pack()
   btns[tr].configure(text=str(i+1))
   btns[tr].pack(side=LEFT)
   td+=1
   if td==3:
      td=0
      tr+=1
   i+=1
window.mainloop()