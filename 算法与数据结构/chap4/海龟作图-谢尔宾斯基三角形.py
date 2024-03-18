import turtle
def sierpinski(degree,points): #degree为阶数，points为坐标点
    colormap=['blue','red','green','white','yellow','orange'] #不同degree对应的颜色
    drawTriangle(points,colormap[degree])
    if degree>0: #此处是用递归来获得每一阶三角形的左、上、右三个顶点的横纵坐标
        sierpinski(degree-1, #左边小三角形的左、上、右三个顶点的横纵坐标
                  {'left':points['left'], #(X左，Y左)
                  'top':getMid(points['left'],points['top']), #((X左+X上)/2，(Y左+Y上)/2)
                  'right':getMid(points['left'],points['right'])}) #((X左+X右)/2，(Y左+Y右)/2)
        sierpinski(degree - 1, #上边小三角形的左、上、右三个顶点的横纵坐标
                  {'left':getMid(points['left'], points['top']),
                   'top':points['top'],
                   'right':getMid(points['top'], points['right'])})
        sierpinski(degree - 1, #右边小三角形的左、上、右三个顶点的横纵坐标
                  {'left':getMid(points['left'],points['right']),
                   'top':getMid(points['top'], points['right']),
                   'right':points['right']})

def drawTriangle(points,color): #具体的顶点坐标points和填充颜色color由sierpinski递归获得
    t.fillcolor(color) #查colormap可得填充颜色color
    t.penup()
    t.goto(points['top']) #画笔移至填充颜色范围的起点
    t.pendown()
    t.begin_fill() #开始填充
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top']) #勾画出填充颜色的范围
    t.end_fill()

def getMid(p1,p2): #每多一阶三角形，边长就缩减为原来的1/2
    return (p1[0]+p2[0])/2,(p1[1]+p2[1])/2

t=turtle.Turtle()
t.speed(0)
t.hideturtle()
points={'left':(-200,-100), #定义大三角形的左、上、右顶点坐标
        'top':(0,200),
        'right':(200,-100)}

sierpinski(5,points)
turtle.done()