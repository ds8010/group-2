import turtle

def setPos(x,y):
    turtle.setheading(headin0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def pattern(hex_color,circle_color,square_color,border_color):
    x=-250
    y=150
    # The first row (hexagon, circle, square)
    setPos(x,y) # the turtle is positioned at (-150,150) on the xy coordinate with heading 0 (to the east)
    hexagon(50,border_color,hex_color) # starting from (-150,150) it draws hexagon with side_length of 50 and the turtle ends at its starting point (-150,150)
    setPos(x+150,y) # this takes the turtle to (0,150)
    circle(50,border_color,circle_color)
    setPos(x+225,y)
    square(90,border_color,square_color)
    
    # The second row (hexagon, circle, square)
    setPos(x+115,y-120)
    hexagon(50,border_color,hex_color)
    setPos(x+265,y-120)
    circle(50,border_color,circle_color)
    setPos(x+340,y-120)
    square(90,border_color,square_color)
    
    # The third row (hexagon, circle, square)
    setPos(x+230,y-240)
    hexagon(50,border_color,hex_color)
    setPos(x+380,y-240)
    circle(50,border_color,circle_color)
    setPos(x+455,y-240)
    square(90,border_color,square_color)

def main():

main()