from pathlib import Path
import csv

GRADES_FILE = Path(__file__).resolve().parent / "grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, compute each student's weighted final
    grade, and print a summary of how many students fall into each
    grade range.
    """
    try:
        weighted_final_list = []
        with open(GRADES_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            for row in reader:
                if row:  # Ensure row is not empty
                    final_grade = process_row(row)
                    weighted_final_list.append(final_grade)
                    
        analyze_grade(weighted_final_list)
        
    except FileNotFoundError:
        print(f"Error: Could not find the file {GRADES_FILE}.")
    except Exception as e:
        print(f"An unexpected error occurred while processing the file: {e}")


def process_row(row):
    """Given one row from the grades file, return that student's
    weighted final grade (bypass the Name and StudentID columns)."""
    # Columns 0 and 1 are Name and StudentID, so slice from index 2 onwards
    scores = row[2:]
   
    numeric_scores = [float(score) for score in scores]
    
    test_scores = numeric_scores[0:4]
    exam_scores = numeric_scores[4:6]
    discussion_scores = numeric_scores[6:8]
    project_score = numeric_scores[8]
    
    test_avg = average_subject(test_scores)
    exam_avg = average_subject(exam_scores)
    discussion_avg = average_subject(discussion_scores)
    
    return weight_final(test_avg, exam_avg, discussion_avg, project_score)


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""
    if not subject_list:
        return 0.0
    return sum(subject_list) / len(subject_list)


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Return a student's weighted final grade, combining the test,
    exam, discussion, and project scores using the weight constants
    declared above."""
    weighted_grade = (
        (test_avg * TEST_WEIGHT) +
        (exam_avg * EXAM_WEIGHT) +
        (discussion_avg * DISCUSSION_WEIGHT) +
        (project_score * PROJECT_WEIGHT)
    )
    return weighted_grade


def analyze_grade(weight_final_list):
    """Count and print how many students fall into each grade range:
    90 or above, 80-89, 70-79, 60-69, and below 60."""
    count_90_above = 0
    count_80_89 = 0
    count_70_79 = 0
    count_60_69 = 0
    count_below_60 = 0
    
    for grade in weight_final_list:
        if grade >= 90:
            count_90_above += 1
        elif grade >= 80:
            count_80_89 += 1
        elif grade >= 70:
            count_70_79 += 1
        elif grade >= 60:
            count_60_69 += 1
        else:
            count_below_60 += 1
            
    print(f"Number of students with final grade 90 or above: {count_90_above}")
    print(f"Number of students with final grade 80–89: {count_80_89}")
    print(f"Number of students with final grade 70–79: {count_70_79}")
    print(f"Number of students with final grade 60–69: {count_60_69}")
    print(f"Number of students with final grade below 60: {count_below_60}")


if __name__ == "__main__":
    main()