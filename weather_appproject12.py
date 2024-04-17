from tkinter import *
from tkinter import ttk # importing the class ttk for combo
import requests

def data_get():
  city = city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={b9c45ce722715f2aa842a24241d941c7}").json()
  wc_label1.config(text= data["weather"][0]["main"])
  wd_label1.config(text= data["weather"][0]["description"])
  temp_label1.confi(text=str(int(data["main"]["temp"]-273.15)))    # covert kelvin to celcius
  pres_label1.config(text=data["main"]["pressure"])




win = Tk()  # make a variable for window and called a class of tkinter
win.title("Weather App")
win.config(background="light blue")
win.geometry("500*500")

name_label =Label(win,text="Python Project Weather App",font =("Poppins",30,"bold")) #label the title and win is jst a parameter
name_label.place(x=25,y=50,height=50,width=450)# placing the text in x-axis y-axis and height

city_name = StringVar
list_names =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Python Project Weather App",values = list_names,font =("Poppins",30,"bold"),text_variable = city_name)
com.place(x=25,y=120,height=50,width=450)  # having list of searching for states

#box for weather climate see in output
wc_label =Label(win,text="Weather Climate",font =("Poppins",20,)) 
wc_label.place(x=25,y=260,height=50,width=210)
# side box of it
wc_label1 =Label(win,text=" ",font =("Poppins",20,)) 
wc_label1.place(x=250,y=260,height=50,width=210)

#box for weather desc see in output
wd_label =Label(win,text="Weather Description",font =("Poppins",20)) 
wd_label.place(x=25,y=330,height=50,width=210)

#side box of it
wd_label1 =Label(win,text=" ",font =("Poppins",20)) 
wd_label1.place(x=250,y=330,height=50,width=210)

#box for temperature
temp_label =Label(win,text="Temperature",font =("Poppins",20)) 
temp_label.place(x=25,y=400,height=50,width=210)

#box of it
temp_label1 =Label(win,text=" ",font =("Poppins",20)) 
temp_label1.place(x=250,y=400,height=50,width=210)
 
#box for pressure
pres_label =Label(win,text="Pressure",font =("Poppins",20)) 
pres_label.place(x=25,y=470,height=50,width=210)

#box of it
pres_label1 =Label(win,text=" ",font =("Poppins",20)) 
pres_label1.place(x=250,y=470,height=50,width=210)

#done button
done_button = Button(win,text="Done",font =("Poppins",20,"bold"),command = data_get)
done_button.place(y=190,x=200,width=100,height=50)

win.mainloop()
