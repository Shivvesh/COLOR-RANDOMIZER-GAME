from tkinter import * 
import random

root = Tk()
root.title("COLOR RANDOMIZER GAME")
root.geometry("650x500")

colour_label = Label(root, font = ("Lucida Sans", 50, "bold", "italic"))
colour_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def RANDOMIZER():
    text_names = ["YELLOW", "BLACK", "BLUE", "GREEN", "RED", "ORANGE"]
    text_name = random.randint(0,5)
    
    fg_names = ["yellow", "black", "blue", "red", "orange", "green", "purple"]
    fg_name = random.randint(0,6)
    
    colour_label["text"] = text_names[text_name]
    colour_label["fg"] = fg_names[fg_name]
    
btn = Button(root, text = "START", bg="dark olive green", fg = "white", relief=FLAT,  padx=10, pady=1,  font=("Arial",15), command = RANDOMIZER)
btn.place(relx = 0.5, rely = 0.7, anchor = CENTER) 
    
    
root.mainloop()