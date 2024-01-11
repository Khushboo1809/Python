from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime

# import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getweather():
    city = textfield.get()

    geolocator = Nominatim(usr_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # weather


# search box
Search_image = PhotoImage(file="")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"))
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="")
myimage_icon = Button(
    image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather
)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file="")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# botton box
Frame_image = PhotoImage(file="")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)


# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)


# label
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="blue")
label1.place(x=120, y=400)


label2 = Label(
    root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="blue"
)
label2.place(x=250, y=400)

label3 = Label(
    root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="blue"
)
label3.place(x=430, y=400)

label4 = Label(
    root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="blue"
)
label4.place(x=650, y=400)


t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 15, "bold"), bg="blue")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 15, "bold"), bg="blue")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 15, "bold"), bg="blue")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 15, "bold"), bg="blue")
p.place(x=670, y=430)

root.mainloop()
