from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("radiobutton")
root.geometry("1000x500")
def order():
    print(f"we have received your{var.get()} order")
    
    
var=IntVar()
var.set("Radio")
Label(root,text="what would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="dosa",padx=14,variable=var,value=1).pack(anchor="w")
rdio=Radiobutton(root,text="dosa",padx=14,variable=var,value=2).pack(anchor="w")

radio=Radiobutton(root,text="idly",padx=14,variable=var,value=3).pack(anchor="w")

radio=Radiobutton(root,text="chutney",padx=14,variable=var,value=4).pack(anchor="w")

radio=Radiobutton(root,text="maggie",padx=14,variable=var,value=5).pack(anchor="w")
Label(root,text="\n\n").pack()
Button(text="submit",command=order).pack()

root.mainloop()
