# Program to calculate a Student's grade in two decimal places with validation.

# Weight constants
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# Range bounds constants
EXAM_MAX = 100
ASSIGNMENT_MAX = 30
QUIZ_MAX = 20

# Prompts and inputs
midterm_exam_grade = float(input("Please enter midterm grade 0-100: "))
final_exam_grade = float(input("Please enter final exam grade 0-100: "))
assignment_one = float(input("Please enter first assignment grade 0-30: "))
assignment_two = float(input("Please enter second assignment grade 0-30: "))
quiz_one = float(input("Please enter first quiz grade 0-20: "))
quiz_two = float(input("Please enter second quiz grade 0-20: "))

# Initialize category scores to 0.0
exam_grade = 0.0
assignment_grade = 0.0
quiz_grade = 0.0

# 1. Test the midterm and final exam grades are within the valid range
if 0 <= midterm_exam_grade <= EXAM_MAX and 0 <= final_exam_grade <= EXAM_MAX:
    # calculate the exam grade
    exam_grade = ((midterm_exam_grade + final_exam_grade) / 2) * EXAM_WEIGHT
else:
    # print invalid input for exams
    print("Invalid input. Please enter exams within the 0-100 range.")

# 2. Test the assignment grades are within the valid range
if 0 <= assignment_one <= ASSIGNMENT_MAX and 0 <= assignment_two <= ASSIGNMENT_MAX:
    # calculate the assignment grade
    assignment_grade = (((assignment_one + assignment_two) / (ASSIGNMENT_MAX * 2)) * 100) * ASSIGNMENT_WEIGHT
else:
    # print invalid input for assignments
    print("Invalid input. Please enter assignments within the 0-30 range.")

# 3. Test the quiz grades are within the valid range
if 0 <= quiz_one <= QUIZ_MAX and 0 <= quiz_two <= QUIZ_MAX:
    # calculate the quiz grade
    quiz_grade = (((quiz_one + quiz_two) / (QUIZ_MAX * 2)) * 100) * QUIZ_WEIGHT
else:
    # print invalid input for quizzes
    print("Invalid input. Please enter quizzes within the 0-20 range.")

# 4. Add the final grade
final_grade = exam_grade + assignment_grade + quiz_grade

# Output final result
print(f"The students final grade is {final_grade:.2f}%")