# tkinter library
from tkinter import *
import covid_scrape as covids
# declares UI display window
window = Tk()
scroll = Scrollbar(window)
# creates a label with text, background and foreground colors, height, and width
stats = Label(
   text=f'COVID-19 World-Wide Stats\n\n{covids.find_stats()}',
   bg='black',fg='red',
   height=100,width=100)
# creates a user input module
entry = Entry()
# creates a button with text
clicker = Button(text="wow")
# appends the greeting label to the UI
stats.pack()
scroll.pack(side = RIGHT,fill = Y)
entry.pack()
clicker.pack()
# initializes the window instance
window.mainloop()