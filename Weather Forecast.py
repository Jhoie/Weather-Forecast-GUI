# weather forecast using open weather api

import tkinter
from tkinter import font
from PIL import ImageTk, Image  # this method is needed to get other formats of images other than png and ppm.
import requests

def format_response(weather):
    try:
        name = (weather["city"]["name"])
        desc = (weather["list"][0]['weather'][0]["description"])
        temp = (weather["list"][0]['main']["temp"])

        result = "City: %s \nConditions: %s \nTemperature(°F): %s "% (name, desc, temp)

    except:
        result = "Invalid Input"

    return result

def get_weather(city):
    weather_key = "6a2027398d0268a79019eccaaad02c16"
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"APPID": weather_key, "q":city, "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()

    label["text"]=format_response(weather)


HEIGHT = 400
WIDTH = 400

root = tkinter.Tk()
canvas = tkinter.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

# cloud image
img = ImageTk.PhotoImage(Image.open("pero-kalimero-9BJRGlqoIUk-unsplash.jpg"))

background_label = tkinter.Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

frame = tkinter.Frame(root, bg="#88c1ff", bd=2)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.08)

entry = tkinter.Entry(frame, bg= "white", font="bold")
entry.place(x=3, relwidth=0.83, relheight=1)

button = tkinter.Button(frame, text="Click", fg="red", command=lambda: get_weather(entry.get()))  # makes the button functional
button.place(relx=0.85, relwidth=0.15, relheight=1)

low_frame = tkinter.Frame(root, bg="#659ec7", bd=5)
low_frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.65)

label = tkinter.Label(low_frame, font =("Courier", 13))
label.place(relwidth=1, relheight=1)

root.mainloop()
