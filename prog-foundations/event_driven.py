#waiting until an event occurs

import time
import tkinter

#handler for time event
def alarm():
    print('Calling the Pizza Guy ....')

#handler for ringing doorbell
def doorbell():
    print('Ding Dong !!')
    time.sleep(1)
    print('Opening the Door ...')

#handler when the phone rings

def phonecall():
    print('Answering the phone ..')


#create buttons and assign callbacks

root = tkinter.Tk()
tkinter.Button(root, text = 'Ring Doorbell', command = doorbell).pack()
tkinter.Button(root, text = 'Call Phone', command = phonecall).pack()

root.after(4000, alarm)

root.mainloop()


######