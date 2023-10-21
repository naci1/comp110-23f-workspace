from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle() #makes the turtle invisible
leo.penup()
leo.goto(-150,-50)
leo.pendown() #begins drawing once again

i : int = 0
leo.begin_fill()
leo.pencolor(255,0,0) #this is pure red
leo.fillcolor(128,128,128) #This is gray. All the RGB values are half of the red,blue, and green.
while(i < 3):
    leo.forward(250)
    leo.left(120) #changed from square to triangle
    i = i+1
leo.end_fill()

bob: Turtle = Turtle()
bob.speed(100)
bob.hideturtle()
bob.penup()
bob.goto(-150,-50)
bob.pendown()

j:int = 0
bob.begin_fill()
bob.pencolor(0,255,0) #bob's color is now green
bob.fillcolor(255,255,255) #bob's fill color is completely black

side_length: int = 300 #bigger size
while j < 5: #changed loops of second triangle to a much larger number
    bob.forward(side_length)
    side_length = side_length * 0.96 #decreasing side length
    bob.left(121)
    i = i + 1
leo.end_fill()
done()


  