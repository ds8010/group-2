"""Group: 2
   Author1:Yosef Shibele
   Part: Contributed with the "pattern" function and the "main" function and also add "go_to_east" function to make the pattern function more better. And helped with the comments.

   Author2:Hamad Alsaadi 
   Part: Contibuted with the "square" function and the "setPos" function, also the comments for the 2 functions.

   Author3:Dona Pal
   Part: Contributed with the "hexagon" and "circle" functions. Also helped with the comments. 

   Visit our github group repository: https://github.com/ds8010/group-2

   Manifesto: This is a program is written to draw a hexagon, circle and square in a pattern in a row; and repeat the pattern two more times at different positions. 
   
   CODE COMPLETED"""


from turtle import Turtle, Screen

def hexagon(turta,side_length,border_color,hexa_color):
    """Draws hexagon with a given side_lengh and a given border_color and fills it with a given hex_color."""
    
    turta.color(border_color)
    turta.fillcolor(hexa_color)
    turta.begin_fill()
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.end_fill()

def circle(turta,radius,border_color,circle_color):
    """Draws a circle with a given radius and a given border_color and fills it with a given circle_color."""
    turta.color(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(radius)
    turta.end_fill()

def square(turta,side_length,border_color,square_color):
    """Draws square with a give side_length and a given border_color and fills it with a given square_color."""
    turta.color(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.forward(side_length)
    turta.left(90)
    turta.forward(side_length)
    turta.left(90)
    turta.forward(side_length)
    turta.left(90)
    turta.forward(side_length)
    turta.end_fill()


def setpos(turta,x,y): 
    """Sets the turtle to the given x and y coordinate value without any trace."""
    turta.setheading(0)
    turta.penup()
    turta.goto(x,y)
    turta.pendown() 

def go_to_east(turta,distance):
    """
    distance -> float
    Takes the turtle 'distance' units to the east without any trace. """
    turta.setheading(0)
    turta.penup()
    turta.forward(distance)
    turta.pendown()

def pattern(turta, row_height, hexa_color, circle_color, square_color, border_color): # by passing the row_heght parameter, this function is able to make the shapes with differnt size.
    """
    row_height: determines how wide is the row of the shapes. It is, actually, the diameter of the circle or the length of the square.
    
    Draws a hexagon filled with  hexa_color color first followed by a circle filled with circle_color then followed by a square filled with square_color with a given row_heght
    
     """
    hex_side_length = (5/9)*row_height
    circle_radius = 0.5*row_height
    square_side_length = row_height
    
    hexagon(turta, hex_side_length, border_color, hexa_color)
    go_to_east(turta, 2.5*hex_side_length + 25)  # 25 is the gap between the hexagon and the circle
    circle(turta, circle_radius, border_color, circle_color)
    go_to_east(turta, hex_side_length + 25) # 25 is the gap between the hexagon and the circle
    square(turta, square_side_length, border_color, square_color)

def main():
    Hexa_color = input('Enter the color what you want to fill the hexagon with: ')
    Circle_color = input('Enter the color what you want to fill the circle with: ')
    Square_color = input('Enter the color what you want to fill the square with: ')
    Border_color = input('Enter the color what you want for the border of the shapes: ')
    turta = Turtle()
    win = Screen()
    win.bgcolor("Skyblue")
    turta.speed(0)
    setpos(turta,-250,150) 
    pattern(turta,90, Hexa_color, Circle_color, Square_color, Border_color) 
    setpos(turta,-150,40)
    pattern(turta,90,Hexa_color, Circle_color, Square_color, Border_color)
    setpos(turta,-50,-70)
    pattern(turta,90,Hexa_color, Circle_color, Square_color, Border_color)
    win.exitonclick()

main()
