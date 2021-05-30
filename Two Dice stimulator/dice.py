import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('450x450')
root.title('Python Dice Game')


l0 = tkinter.Label(root, text="")
l0.pack()

l1 = tkinter.Label(root, text="TWO DICE ROLLING STIMULATOR", fg = "Blue",
       
        font = "Helvetica 18 bold italic")
l1.pack()

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label1.image = image1

label1.pack( expand=True)



dice2 = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

image2 = ImageTk.PhotoImage(Image.open(random.choice(dice2)))

label2 = tkinter.Label(root, image=image2)
label2.image = image2

label2.pack( expand=True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice2)))
    label1.configure(image=image1)
    label1.image = image1
    label2.configure(image=image2)
    label2.image = image2
    
          

         
button = tkinter.Button(root, text='Roll the Dices', fg='Blue',command=rolling_dice,font = "Helvetica 18 bold italic")
button.pack( expand=True)
if image1 == image2:
       l = tkinter.Label(root, text="Dice Rolling Stimulator", fg = "Blue",bg = "yellow",font = "Helvetica 16 bold italic")
       l.pack()

root.mainloop()