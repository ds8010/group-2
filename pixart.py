import turtle as t
def pixel(color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(30)
    for i in range(4):
        t.right(90)
        t.forward(30)
    t.end_fill()



def row(column,color):
    for i in range(column):
        pixel(color)
        

def grid():
    x,y = -300 , 300
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(20):
        for i in range(20):
            pixel('white')
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(600)
        t.setheading(0)


def square(row,column,size,color='green'):
    t.penup()
    t.goto(-size/2,size/2)
    t.pendown()
    for i in range(row):
        for i in range(column):
            pixel(color)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(size)
        t.setheading(0)


def rectangle(row,column,length,width,color='orange'):
    t.penup()
    t.goto(-length/2,width/2)
    t.pendown()
    for i in range(row):
        for i in range(column):
            pixel(color)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(length)
        t.setheading(0)

t.tracer(False)
grid()
rectangle(5,10,300,150)
t.done()
