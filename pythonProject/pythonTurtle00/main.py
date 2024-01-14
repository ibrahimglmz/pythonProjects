import  turtle
drawing_borad = turtle.Screen()
drawing_borad.bgcolor("green")
drawing_borad.title("deneme python")
turtle_instance = turtle.Turtle()

def turtle_forward():
   turtle_instance.forward(50)

def turtle_right():
   turtle_instance.right(25)

def turtle_left():
   turtle_instance.left(25)



def kordinat_turtle():
   turtle_instance.goto(10,10)
   turtle_instance.clear()


drawing_borad.listen()
drawing_borad.onkey(fun=turtle_forward, key="space")
drawing_borad.onkey(fun=turtle_forward, key="w")
drawing_borad.onkey(fun=turtle_left, key="d")
drawing_borad.onkey(fun=turtle_right, key="a")
drawing_borad.onkey(fun=kordinat_turtle, key="k")




turtle.mainloop()


