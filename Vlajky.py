import tkinter

canvas = tkinter.Canvas(bg='sky blue', width=400,height=400)
canvas.pack()

canvas.create_rectangle(50,50,50+135,50+30,fill='black')
canvas.create_rectangle(50,80,50+135,50+60,fill='red')
canvas.create_rectangle(50,110,50+135,50+90,fill='yellow')

canvas.create_rectangle(200,160,200+135,160+30,fill='white')
canvas.create_rectangle(200,190,200+135,160+60,fill='blue')
canvas.create_rectangle(200,220,200+135,160+90,fill='red')

canvas.create_rectangle(50,160,50+45,160+90,fill='blue')
canvas.create_rectangle(50+45,160,50+90,160+90,fill='white')
canvas.create_rectangle(50+90,160,50+135,160+90,fill='red')

canvas.create_rectangle(200,50,200+45,50+90,fill='green')
canvas.create_rectangle(200+45,50,200+90,50+90,fill='white')
canvas.create_rectangle(200+90,50,200+135,50+90,fill='red')


tkinter.mainloop()
