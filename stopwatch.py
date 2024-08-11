from tkinter import * 
from tkinter import messagebox 
import time

window = Tk()
window.geometry("250x200")
window.title("Stop watch")
window.configure(background = "white")
# declaring the object of StringVar() class

hour = StringVar()
minute = StringVar()
second = StringVar()


#setting default values for all 3 objects
hour.set("00")
minute.set("00")
second.set("00")

def submit():
    

hour_entry = Entry(window, textvariable = hour, width = 3, font = ("times", 30))
minute_entry = Entry(window, textvariable = minute, width = 3, font = ("times", 30))
second_entry = Entry(window, textvariable = second, width = 3, font = ("times", 30))

set_conutdon = Button(window, text = "Set time countdown")

hour_entry.grid(row = 1, column = 1, pady = 30, padx = 20)
minute_entry.grid(row = 1, column = 2)
second_entry.grid(row = 1, column = 3, padx = 20)
set_conutdon.place(x = 50, y = 120)



window.mainloop()
