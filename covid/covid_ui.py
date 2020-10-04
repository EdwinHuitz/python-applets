# tkinter library
from tkinter import *
import covid_scrape as covids
# declares UI display window
window = Tk()
window.title('COVID-19 World-Wide Statistics')
window.configure(bg='black')
cStats = str(covids.find_stats()).split('|')
frame = Frame(master=window,bg='black')
wrld = cStats[2].replace(' population:\n','')
stats = Label(master=window,text=f'World-Wide {wrld}',bg='black',fg='white')
stats.pack()
Label(master=window,text='Top Ten Countries Affected by COVID-19',bg='black',fg='white').pack()
frame.pack(padx=10,pady=10)
a=0
b=4
def info(x):
   num=int(x)
   stats.configure(text=f'{cStats[num-1]}{cStats[num]}')

while a < len(cStats)/18:
   r=0
   while r < 5:
      block = Button(frame,text=f'{cStats[b-1]}{cStats[b]}',width=14,height=3,command=lambda a=f'{b+1}':info(a))
      block.grid(row=a,column=r,padx=5,pady=5)
      r+=1
      if b< len(cStats)-3:
         b+=3
   a+=1

# initializes the window instance
window.mainloop()