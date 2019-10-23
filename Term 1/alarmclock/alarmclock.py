import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

h = 0
m = 0
s = 0
t = "AM"
def get_alarm(*args):
    global h
    h = input("What hour? ")
    global m
    m = input("What minute? ")
    global s
    s = input("What second? ")
    global t
    t = input("AM or PM? ")

def quit(*args):
    root.destroy()

def beep():
    winsound.Beep(650, 5000)
def alarm():
    get_alarm()
    
def current_time():
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds%60
    if currentSecond < 10:
        currentSecond = "0" + str(currentSecond)

    totalMinutes = totalSeconds//60
    currentMinute = totalMinutes%60
    if currentMinute < 10:
        currentMinute = "0" + str(currentMinute)

    totalHours = totalMinutes//60
    currentHour = (totalHours%24)-6

    am_pm = ""
    if currentHour >= 12:
        am_pm = "PM"
    if currentHour == 0:
        currentHour = currentHour+12
    else:
        am_pm = "AM"
        if currentHour == 0:
            currentHour = currentHour + 12
    a = str(h) + ":" + str(m) + ":" + str(s) + t

    timex = str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond) + " " + am_pm
    if timex == a:
        beep
    return timex
def show_time():
    global h
    global m
    global s
    global t
    time = current_time()
    txt.set(time)
    root.after(1000, show_time)

root = Tk()

#set window size
root.geometry("500x200")
root.attributes("-fullscreen", False)
root.configure(background = 'Gray9')

#set up keys to do an alarm or quit
root.bind("x", quit)
root.bind("a", get_alarm)

#set up font
root.after(1000, show_time)
fnt = font.Font(family = "Calibri", size = 60, weight = "bold")
txt = StringVar()

#display time and set up the colors of text and background
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "steel blue", background = "gray9")

#place the time in the center of the screen
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#start main loop
root.mainloop()

get_alarm()
