START_ROWS = 7
END_ROWS = 0
STEP = -1

for row in range(START_ROWS, END_ROWS, STEP):

    for col in range(row):
        print("*", end="")

    print()