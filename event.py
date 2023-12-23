from tkinter import *
def swati(event):
    print(f"you clicked on the button at{event.x},{event.y}")
    label.config(text="Code never lies, comments sometimes do", font=('Helvetica 17 bold'))
root=Tk()
root.title("events in tkinter")
root.geometry("655x455")
label= Label(root, text= "")
label.pack(pady= 50)
widget=Button(root,text="click me")
widget.pack()
widget.bind('<Button-1>',swati)
root.mainloop()
