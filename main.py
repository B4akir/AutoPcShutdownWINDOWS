from tkinter import *
from time import *
import datetime
import os

#UPDATING THE CLOCK
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    window.after(1000, update)

# COUNTING DOWN WHEN THE PC WILL SHUTDOWN
def countdown2(desired_time):
    if called==2: # CALLED IS USED TO DETERMINE IF THE USER HAS CLICKED SUBMIT OR CANCEL, DEPENDING ON THE SITUATION THE APPROPRIATE COUNTDOWN WILL RUN (1 OR 2)
        time_diff = desired_time - datetime.datetime.now()
        total_minutes = time_diff.seconds // 60
        hours = total_minutes // 60
        minutes = total_minutes % 60
        time1 = ("Your pc will shutdown in {} hours and {} minutes:".format(hours, minutes, ))
        countdown.config(text=time1)
        window.after(100, countdown2, desired_time)
    else:
        pass #THIS IS TO ENSURE THE CANCEL BUTTON WORKS

#SHOWING THE USER WHEN THE PC WILL SHUTDOWN, ACCORDING TO THEIR SPINBOX INPUT
def countdown1():
    h = int(sati.get())
    m = int(minute.get())
    total_seconds = h * 3600 + m * 60
    time_diff = datetime.timedelta(seconds=total_seconds)
    current_time = datetime.datetime.now()
    desired_time = current_time + time_diff

    if called == 1:
        time1 = "Your pc will shutdown in: " + str(h) + " hours and " + str(m) + " minutes"
        countdown.config(text=time1)
        window.after(10, countdown1)
    elif called == 2:
        countdown2(desired_time)

# INITIANILIZING THE SHUTDOWN
def submit():
    global called
    called = 2
    h = int(sati.get())
    m = int(minute.get())
    vrijeme = (h * 3600) + (m * 60)
    os.system("shutdown /s /t " + str(vrijeme))

#CANCELING THE SHUTDOWN
def cancel():
    global called
    called=1
    os.system("shutdown /a")
    countdown1()

window = Tk()

# CLOCK
time_label = Label(window, font=("Arial", 10), fg="#00FF00", bg="black", )
time_label.place(x=510, y=70)

# SPINBOX
minute = Spinbox(window, from_=0, to=60, width=3, font=("Helvetica", 12), wrap=True)
sati = Spinbox(window, from_=0, to=60, width=3, font=("Helvetica", 12), wrap=True)
minute.place(x=410, y=100)
sati.place(x=320, y=100)

# SPINBOX LABELS
hours = Label(window, text="Hour/s").place(x=360, y=100)
minutes = Label(window, text="Minute/s").place(x=450, y=100)

# SHUTDOWN IN:
countdown = Label(window, font=("Arial", 20), text="Your pc")
countdown.pack()

submit = Button(window, text="SHUTDOWN", font=("Arial", 10), command=submit).place(x=490, y=300)
cancel= Button(window, text="CANCEL", font=("Arial", 10), command=cancel).place(x=420, y=300)

# CALLING FUNCTIONS AND OTHER FUNCTION STUFF
called = 1
countdown1()
update()

window.geometry("600x350")
window.resizable(False, False)
window.mainloop()
