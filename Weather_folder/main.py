from tkinter import *
from tkinter import font
import requests 

HEIGHT = 500
WIDTH = 600


def Test_function(entry):
    print('This entry is:', entry)

#8d05c20a298c95eb673f31dd025fd55e
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key} 

def Format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'Please Enter a valid City of The world.'
        #\nIf there is an issue with this,\nPlease fuck off and use BBC insted.\nIm not a Mirical worker nor can I spell.\nI am only 14 years old and I have\nenough stress on my mind.\n\nKindly Piss off.'

    return final_str


def Get_weather(city):
    weather_key = '8d05c20a298c95eb673f31dd025fd55e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = Format_response(weather)



root = Tk()
root.title('Weather App')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file='landscape.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1,relheight=1)    


frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5,rely=0.1,relheight=0.1, relwidth=0.75, anchor='n')

entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1, )

button = Button(frame, text='Search', font=30, command=lambda: Get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.25, )

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=40, anchor='nw', justify='left', bd = 3)
label.place(relwidth=1, relheight=1)


root.mainloop()