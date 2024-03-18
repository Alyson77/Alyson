import turtle

t1=turtle.Turtle()
t1.forward(100)

t2=turtle.Turtle()
t2.forward(200)

t3=turtle.Turtle()
for i in range(4):
    t3.forward(100)
    t3.right(90)

t4=turtle.Turtle()
t4.pencolor('red')
t4.pensize(3)
for i in range(5):
    t4.forward(100)
    t4.right(144)
t4.hideturtle()

t5=turtle.Turtle()
def drawSpiral(t5,lineLen):
    if lineLen>0:
        t5.forward(lineLen)
        t5.right(90)
        drawSpiral(t5,lineLen-5)
drawSpiral(t5,100)




turtle.done()