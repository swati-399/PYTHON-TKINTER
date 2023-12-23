from tkinter import *
import tkinter.messagebox as tms
def help():
    print("i will")
    a=tms.showinfo("help","she will help you")
    print(a)
def rate():
    value=tms.askquestion("how is your experience?","narrate your experience")
    print(value)
root=Tk()
root.title("message box in tkinter")
root.geometry("655x455")
menus=Menu(root)
m1=Menu(menus)
m1.add_command(label="help",command=help)
m1.add_command(label="rate",command=rate)
m1.add_command(label="save")
m1.add_command(label="quit")
root.config(menu=menus)
menus.add_cascade(label="file",menu=m1)


root.mainloop()
