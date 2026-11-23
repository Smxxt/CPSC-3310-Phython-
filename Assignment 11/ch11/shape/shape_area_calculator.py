from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

def main():
    # Store shape objects in a list and process them polymorphically
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Rectangle(4, 4),
        Circle(1.5),
    ]

    print("Areas of various shapes:")
    for shape in shapes:
        # Python resolves shape.area() dynamically based on the object's actual class
        print(f"{shape} {shape.area():.2f}")


if __name__ == "__main__":
    main()