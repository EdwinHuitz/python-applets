# tkinter library
from tkinter import *
import covid_scrape as covids
# declares UI display window
window = Tk()
cStats = str(covids.find_stats()).split('|')
print(len(cStats))
frame = Frame(master=window)
stats = Label(master=window,text=f'COVID-19 World-Wide Stats\n\n{cStats[0]}')
stats.pack()
frame.pack()
a=0
b=1
while a < len(cStats):
   r=0
   while r < 5:
      block = Label(master=frame,text=cStats[b])
      block.grid(row=a,column=r)
      r+=1
      if b< len(cStats)-1:
         b+=1
   a+=1
# initializes the window instance
window.mainloop()