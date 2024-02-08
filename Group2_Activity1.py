from turtle import Turtle, Screen

def go_to_east(turta,distance):
    """
    distance -> float
    Takes the turtle 'a' units to the east without any trace. """
    turta.setheading(0)
    turta.penup()
    turta.forward(distance)
    turta.pendown()

def pattern(turta,row_width,hexa_color, circle_color, square_color, border_color):
    """
    row_widtht: is how big is the row. It is, actually, the diameter of the circle.
    Example (row_width of 100 draws the row of the pattern with width 100)
    
    Draws a hexagon filled with  hexa_color color first followed by a circle filled with circle_color then followed by a square filled with square_color.
    
    And the side_length of the hexagon and the radius of the circle are equal . And also the side_lengh of the square is equal to the side_length of the hexagon multiplied by 1.9. """
    hex_side_length = 0.5*row_width
    circle_radius = 0.5*row_width
    square_side_length = hex_side_length*1.9

    hexagon(turta,hex_side_length,border_color,hexa_color)
    go_to_east(turta, 2.5*hex_side_length + 25)
    circle(turta,circle_radius,border_color,circle_color)
    go_to_east(turta,hex_side_length + 25)
    square(turta,square_side_length,border_color,square_color)

def main():
    Hexa_color = input('Enter the color what you want to fill the hexagon with: ')
    Circle_color = input('Enter the color what you want to fill the circle with: ')
    Square_color = input('Enter the color what you want to fill the square with: ')
    Border_color = input('Enter the color what you want for the border of the shapes: ') 
    turta = Turtle()
    win = Screen()
    turta.speed(0)
    win.bgcolor('Skyblue')
    pattern(turta,100,Hexa_color, Circle_color, Square_color,Border_color)
    pattern(turta,100, Hexa_color,Circle_color,Square_color,Border_color)
    pattern(turta,100,Hexa_color,Circle_color,Square_color,Border_color)
    win.exitonclick()

main()
