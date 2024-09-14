import turtle

def foward_turtle():
    turtle.setheading(90)
    turtle.forward(50)

def backward_turtle():
    turtle.setheading(270)
    turtle.forward(50)

def right_turtle():
    turtle.setheading(0)
    turtle.forward(50)

def left_turtle():
    turtle.setheading(180)
    turtle.forward(50)


def restart():
    turtle.reset()



turtle.shape('turtle')
turtle.onkey(restart,'Escape')
turtle.onkey(foward_turtle,'w')
turtle.onkey(backward_turtle,'s')
turtle.onkey(left_turtle,'a')
turtle.onkey(right_turtle,'d')

turtle.listen()
turtle.mainloop()
