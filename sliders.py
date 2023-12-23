from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("655x455")
def getdollar():
    print(f"we have credited{slider1.get()}dollars to your bank account")
    tmsg.showinfo("account credited",f"we have credited{slider1.get()}dollars to ur account")
slider1=Scale(root,from_=0,to=100,orient=HORIZONTAL)
slider1.pack()
Button(root,text="get dollars",command=getdollar).pack()
root.mainloop()
