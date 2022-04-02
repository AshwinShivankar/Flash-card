import random
from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
random_words = {}
dic_data = {}

try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/french_words.csv")
    dic_data = orignal_data.to_dict(orient="records")
else:
    dic_data = data.to_dict(orient="records")


def change():
    global random_words,timer
    window.after_cancel(timer)
    random_words = random.choice(dic_data)
    canvas.itemconfig(title_name, text= "French",fill="black")
    canvas.itemconfig(title_word, text=random_words["French"],fill="black" )
    canvas.itemconfig(background,image=image)
    timer = window.after(3000,func=flip)


def flip():
    canvas.itemconfig(title_name, text="English",fill="white")
    canvas.itemconfig(title_word, text=random_words["English"],fill="white")
    canvas.itemconfig(background,image=image_2)

def known():
    dic_data.remove(random_words)
    data_2 = pandas.DataFrame(dic_data)
    data_2.to_csv("data/word_to_learn.csv",index=False)
    change()



window = Tk()
window.title("Flashy")
window.config(padx=50,pady=30,bg=BACKGROUND_COLOR)
timer = window.after(3000,func=flip)

canvas = Canvas(width=800, height=510)
image = PhotoImage(file="images/card_front.png")
image_2 = PhotoImage(file="images/card_back.png")
background  = canvas.create_image(400, 263, image=image)
title_name = canvas.create_text(400, 140, text="Title", font=("Arial", 40, "italic"))
title_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)






image_3 = PhotoImage(file="images/right.png")
button = Button(image=image_3,bg=BACKGROUND_COLOR, highlightthickness=0,command=known)
button.grid(column=1,row=1)

image_4 = PhotoImage(file="images/wrong.png")
button_2 = Button(image=image_4,bg=BACKGROUND_COLOR, highlightthickness=0,command=change)
button_2.grid(column=0,row=1)

label = Label(bg=BACKGROUND_COLOR)
label_2 =label.config(text="0:0")


change()

canvas.mainloop()

