import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"


def main():
    choice = ""
    while choice != QUIT:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == SQUARE:
            x = float(input("Enter the starting X coordinate: "))
            y = float(input("Enter the starting Y coordinate: "))
            side = float(input("Enter the length of a side: "))
            color = input("Enter the fill color: ").strip()
            square(x, y, side, color)

        elif choice == CIRCLE:
            x = float(input("Enter the X coordinate of the center: "))
            y = float(input("Enter the Y coordinate of the center: "))
            radius = float(input("Enter the radius: "))
            color = input("Enter the fill color: ").strip()
            circle(x, y, radius, color)

        elif choice == TRIANGLE:
            x = float(input("Enter the starting X coordinate: "))
            y = float(input("Enter the starting Y coordinate: "))
            side = float(input("Enter the length of a side: "))
            color = input("Enter the fill color: ").strip()
            equilateral_triangle(x, y, side, color)

        elif choice == QUIT:
            print("Exiting the program.")

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    turtle.done()


def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")


def square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()


def equilateral_triangle(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()


def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius) 
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


if __name__ == "__main__":
    main()