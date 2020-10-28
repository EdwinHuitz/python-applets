# tkinter library
from tkinter import *
#matplot library
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#panda
from pandas import DataFrame
#regex
import re
import covid_scrape as covids
#global variables
a=0
b=4
chart={'cat':[],'val':[]}
window = Tk()
cStats = str(covids.find_stats()).split('|')
statL = []
for cs in cStats:
   ans = cs.replace('\n','\n\n')
   statL.append(ans)
top,center,bottom = Frame(master=window,bg='black'),Frame(master=window,bg='black'),Frame(master=window,bg='black')
curChart = FigureCanvasTkAgg(plt.Figure(figsize=(1,1)))
curChart.get_tk_widget().pack(side=RIGHT)
#functions
def sorting(item):
   num=int(item)
   chart['cat']=[]
   chart['val']=[]
   inf = cStats[num].split('\n  ')
   inf.pop(0)
   inf[1],inf[3],inf[6]=inf[1].replace('s ',''),inf[3].replace('s ',''),inf[6].replace('\n','')
   for i in inf[1:7]:
      item = i.split(':')
      item[1]=item[1].replace(',','').replace('+','').replace('N/A','0')
      x= re.search("[0-9]",item[1])
      if x==None:
         item[1]=0
      chart['cat'].append(item[0])
      chart['val'].append(int(item[1]))

def info(x):
   global curChart
   try:
      curChart.get_tk_widget().pack_forget()
   except AttributeError:
      pass
   fig = plt.Figure(dpi=100,facecolor='black')
   bars = FigureCanvasTkAgg(fig,top)
   ax = fig.add_subplot(111,facecolor='black')
   num=int(x)
   
   if num == 2:
      wrld = statL[2].replace(' population:\n','')
      stats.configure(text=f'World-Wide {wrld}')
   else:
      stats.configure(text=f'{cStats[num-1]}{statL[num]}')
   sorting(num)
   #building graph
   df = DataFrame(chart,columns=['cat','val'])
   df = df.groupby('cat').sum()
   #new cases
   df1 = df[0:3]
   #total cases
   df2 = df[3:6]
   df1.plot(xlabel='',ylabel='',kind='bar',legend=False,ax=ax,fontsize=8,rot=0,color='r').tick_params(colors='white')
   bars.get_tk_widget().pack(side='left')
   bars.draw()
   curChart=bars

# UI display window
window.iconbitmap('images/covid.ico')
window.title('COVID-19 World-Wide Statistics')
window.configure(bg='black')
stats = Label(master=top,bg='black',fg='white',font=50)
stats.pack(side='right')
info(2)
Button(center,text=f'{cStats[0]}{cStats[1]}',width=14,height=2,command=lambda a=f'{2}':info(2)).pack()
Label(master=center,text='Top Ten Countries Affected by COVID-19',bg='black',fg='white',font=50).pack(side=TOP)
top.pack()
center.pack()
bottom.pack(padx=10,pady=10)
#buttons
while a < len(cStats)/18:
   r=0
   while r < 5:
      block = Button(bottom,text=f'{cStats[b-1]}{cStats[b]}',width=14,height=2,command=lambda a=f'{b+1}':info(a))
      block.grid(row=a,column=r,padx=5,pady=5)
      r+=1
      if b< len(cStats)-3:
         b+=3
   a+=1

# initializes the window
window.mainloop()