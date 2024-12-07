from tkinter import*
#create a tkinter window
root=Tk()
root.geometry('100x100')
root.title("WELCOME TO TKINTER")
btn=Button(root,text="CLICK ME!!!",bd="6",background="Blue",command=root.destroy)
btn.pack(side="left")
root.mainloop()