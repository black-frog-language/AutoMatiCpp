import tkinter as tk
main =  tk.Tk()
main.title('AutoMatiC++') 
main.geometry('1200x800')
new = tk.Label(main,text = "NEW!",bg = 'green',font = ("Arial",30),width = 10,height =2)
new.place(x = 0, y = 0)
edit = tk.Label(main,text = "EDIT!",bg ='blue',font = ("Arial",30),width = 10,height = 2 )
edit.place(x =230,y =0)
main.mainloop()
