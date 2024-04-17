import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.title("Dice Simulator")
window.geometry("500*500")

dice =["dice1.jpg","dice2.jpg","dice3.jpg","dice4.jpg","dice5.jpg","dice6.jpg",]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 =ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image =image1
label2.image =image2

label1.place(x=0,y=100)
label2.place(x=300,y=100)

def dice_roll():

        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        label1.config(image=image1)
        label1.image =image1

        image2 =ImageTk.PhotoImage(Image.open(random.choice(dice)))
        label2.config(image =image2)
        label2.image =image2

button = tk.button(window,text="Roll",command = dice_roll)
button.place (x=250,y=300)


window.mainloop