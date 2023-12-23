from tkinter import *
root=Tk()
def add():
    lbx.insert(ACTIVE,f"hii")
    
root.geometry("655x455")
root.title("listbox in tkinter")
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"FIRST ITEM OF OUR LISTBOX")
Button(root,text="Add Item",command=add).pack()


root.mainloop()
