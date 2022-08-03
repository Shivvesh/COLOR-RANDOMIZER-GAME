from tkinter import *
import random
root = Tk()
root.title("COLOR RANDOMIZER GAME")
root.geometry("500x400")
root.config(bg="white")
label_score = Label(root, text="Score : 0",font=("Bahnschrift Light",15,"bold") ,bg="white")
label_score.place(relx=0.1,rely=0.1, anchor= CENTER)
label_name = Label(root,font=("Arial",40),bg="white")
label_name.place(relx=0.5,rely=0.3, anchor= CENTER)
input_value = Entry(root)
input_value.place(relx=0.5,rely=0.5, anchor= CENTER)
check_label = Label(root, font=("Comic Sans",10,"bold") ,bg="white")
check_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)
class game:
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["BLACK","PINK","GREEN","BLUE","YELLOW","RED", "PURPLE"]
        self.random_number_for_text = random.randint(0,6)
        self.color = ["black","pink","green","blue","yellow","red", "purple"]
        self.random_number_for_color = random.randint(0,6)
        label_name["text"] =  self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
    def __update_score(self,input_value):
        if(input_value == self.color[self.random_number_for_color]):
            print(self.color[self.random_number_for_color])
            self.__score = self.__score + random.randint(0,10)
            label_score["text"] = "Score : "+str(self.__score)
            check_label["text"] = "GOOD JOB :)"
        else:
            check_label["text"] = "UH O :("
    def get_user_value(self, input_value):
        self.__update_score(input_value)
obj = game()
def getInput():
    value = input_value.get()
    obj.get_user_value(value)
    obj.updateGame()
    input_value.delete(0,END)
btn = Button(root, text="CHECK" ,command=getInput, bg="IndianRed1", fg="white", relief=FLAT,  padx=10, pady=1,  font=("Arial",15))
btn.place(relx=0.35,rely=0.65, anchor= CENTER)
btn = Button(root, text="START" ,command=obj.updateGame, bg="dark olive green", fg="white", relief=FLAT,  padx=10, pady=1,  font=("Arial",15))
btn.place(relx=0.65,rely=0.65, anchor= CENTER)
root.mainloop()