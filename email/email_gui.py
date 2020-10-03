import PySimpleGUI as sg
import send_mail as es

#SIMPLE GUI
sg.theme('LightGreen3')
layout = [
   [sg.Text('From: '),sg.InputText()],
   [sg.Text('To: '),sg.InputText()],
   [sg.Text('Subject: '),sg.InputText()],
   [sg.Text('Message: '),sg.InputText()],
   [sg.Button('submit'),sg.Button('test')]
]
window = sg.Window('Email Sender',layout,margins=(50,100))
while True:
   #checks for events
   event, values = window.read()
   #if the button is pressed or window is closed, the loop is ended
   if event == sg.WIN_CLOSED:
      break
   if event == 'submit':
      es.getValues(values[0],values[1],values[2],values[3])
      sg.popup('Email has been sent!')

#closes the window since the loop has ended
window.close()