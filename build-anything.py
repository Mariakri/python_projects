from tkinter import *
from time import strftime

root = Tk()

root.resizable(0,0)
root.title("python digital Clock")

Label (root,text = 'Python Digital Clock', font = 'arial 20 bold ')
root.geometry("500x100")

def Dclock ():
    string = strftime('%H %M: %S: %p')
    mark.config(text=string)
    mark.after(1000, Dclock)



mark = Label(root, font = ('calibri', 50 ,'bold'), foreground = 'blue', background = 'black')

mark.pack(anchor = 'center')
Dclock()
mainloop()