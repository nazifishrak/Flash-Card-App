BACKGROUND_COLOR = "#B1DDC7"

from tkinter import *
from turtle import width
import pandas
import random

data=pandas.read_csv('./data/french_words.csv')
DELAY=3000
word_list = data.to_dict(orient="records")
random_word_dict ={}



# WINDOW CREATION
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)


 # IMAGES
card_back= PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file= "./images/wrong.png")
   




# CANVAS
canvas = Canvas()
canvas.config(width=800, height= 530,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)
imageCard=canvas.create_image(400,263, image =card_back)





# TEXT
language=canvas.create_text(400,150, text= "Title", font = ("Arial", 40, "italic"),fill="white")
word=canvas.create_text(400,250, text= "Word", font = ("Arial", 65, "bold"))
def next_card():
    global random_word_dict, timer
    window.after_cancel(id=timer)
    random_word_dict = random.choice(word_list)
    french_word = random_word_dict["French"]
    canvas.itemconfig(imageCard, image=card_front)
    canvas.itemconfig(language, text= "French", fill="black")
    canvas.itemconfig(word, text= french_word,fill= "black")
    timer= window.after(DELAY,flipcard)


def flipcard():
    canvas.itemconfig(imageCard, image=card_back)
    english_word = random_word_dict["English"]
    canvas.itemconfig(language, text="English",fill="black")
    canvas.itemconfig(word, text=english_word, fill = "white")

    
    
    

# WRONG BUTTON
wrong_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0,columnspan=1)

# RIGHT BUTTON
right_button = Button(image=right_img,highlightthickness=0,command=next_card)
right_button.grid(row=1,column=1,columnspan=1)




timer= window.after(DELAY,flipcard)
next_card()






window.mainloop()