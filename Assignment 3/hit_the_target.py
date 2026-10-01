# Program: Turtle Hit the Target Game with Directional Hints
import turtle

# Named constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100    # Corner A x-coordinate
TARGET_LLEFT_Y = 100    # Corner A y-coordinate
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# 1. Setup window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw target square
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Reset turtle to launch origin
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# 2. Get user inputs
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate distance and launch
distance = force * FORCE_FACTOR
turtle.setheading(angle)
turtle.pendown()
turtle.forward(distance)

# Target ceiling boundaries (Corner B xcor and Corner C ycor)
target_right_x = TARGET_LLEFT_X + TARGET_WIDTH  # Corner B xcor
target_top_y = TARGET_LLEFT_Y + TARGET_WIDTH    # Corner C ycor

current_x = turtle.xcor()
current_y = turtle.ycor()

# 3. Evaluate hit/miss status
if (TARGET_LLEFT_X <= current_x <= target_right_x) and (TARGET_LLEFT_Y <= current_y <= target_top_y):
    print("You hit the target!")
else:
    print("You missed the target.")
    
    # 4. Provide hints based on final resting position relative to target corners
    if current_x > target_right_x:
        print("Try a lesser angle.")
    elif current_x < TARGET_LLEFT_X:
        print("Try a greater angle.")
        
    if current_y > target_top_y:
        print("Try lesser force.")
    elif current_y < TARGET_LLEFT_Y:
        print("Try more force.")

turtle.done()