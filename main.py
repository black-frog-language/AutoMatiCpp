import tkinter as tk
main =  tk.Tk()
main.title('AutoMatiC++') 
main.geometry('1200x800')
new = tk.Label(main,fg = "blue",text = "NEW!",bg = 'green',font = ("Arial",30),width = 10,height =2)
new.place(x = 0, y = 0)
edit = tk.Label(main,fg = "green",text = "EDIT!",bg ='blue',font = ("Arial",30),width = 10,height = 2 )
edit.place(x =230,y =0)
bgstripe1 = tk.Label(main,bg = "grey",font = ("Arial",7),width  = 1,height=200 )
bgstripe1.place(x = 460,y = 0)
bgstripe2 = tk.Label(main,bg = "grey",font = ("Arial",5),width =115,height=1)
bgstripe2.place(x = 0,y = 400)
value  = tk.Label(main,text = "value",fg = "blue",font = ("Arial",20))
value.place(x = 0,y = 100)
main.mainloop()
