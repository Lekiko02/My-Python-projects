from tkinter import Tk, Label, Entry, Button, PhotoImage
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

class Weather:
    def __init__(self, master):
        master.title("Weather App")
        master.geometry("900x500+300+200")
        master.resizable(False, False)

        self.Search_image = PhotoImage(file="picture/search.png")
        myimage = Label(image=self.Search_image)
        myimage.place(x=20, y=20)

        self.textfield = tk.Entry(master, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
        self.textfield.place(x=50, y=40)
        self.textfield.focus()

        self.Search_icon = PhotoImage(file="picture/search_icon.png")
        myimage_icon = Button(image=self.Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=self.getweather)
        myimage_icon.place(x=400, y=34)

        # logo
        self.Logo_image = PhotoImage(file="picture/logo.png")
        logo = Label(image=self.Logo_image)
        logo.place(x=150, y=100)

        # information box
        self.box_image = PhotoImage(file="picture/box.png")
        box = Label(master, image=self.box_image)
        box.pack(padx=5, pady=5, side="bottom")

        # time
        self.name = Label(master, font=("arial", 15, "bold"))
        self.name.place(x=30, y=100)
        self.clock = Label(master, font=("Helvetica", 20))
        self.clock.place(x=30, y=130)

        # labels
        self.label1 = Label(master, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
        self.label1.place(x=120, y=400)

        self.label1 = Label(master, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
        self.label1.place(x=250, y=400)

        self.label1 = Label(master, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
        self.label1.place(x=430, y=400)

        self.label1 = Label(master, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
        self.label1.place(x=650, y=400)

        self.t = Label(master, font=("arial", 70, "bold"), fg="#ee666d")
        self.t.place(x=400, y=150)
        self.c = Label(master, font=("arial", 15, "bold"))
        self.c.place(x=400, y=250)

        self.w = Label(master, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.w.place(x=120, y=430)
        self.h = Label(master, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.h.place(x=280, y=430)
        self.d = Label(master, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.d.place(x=450, y=430)
        self.p = Label(master, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.p.place(x=670, y=430)

    def getweather(self):
        city = self.textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)

        if location is not None:
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

                if result is not None:
                        home = pytz.timezone(result)
                        local_time = datetime.now(home)
                        current_time = local_time.strftime("%I:%M %p")
                        self.clock.config(text=current_time)
                        self.name.config(text="CURRENT WEATHER")
                else:
                        self.name.config(text="Timezone not found!")
                        self.clock.config(text="")
        else:
                self.name.config(text="Location not found!")
                self.clock.config(text="")


if __name__ == "__main__":   
    root = Tk()
    app = Weather(root)
    root.mainloop()
