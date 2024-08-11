# Student Grades Analysis

def calculate_average(grades):
    return sum(grades) / len(grades)

def student_summary(students):
    for student, subjects in students.items():
        avg_grade = calculate_average(subjects.values())
        print(f"Student: {student}")
        print(f"Average Grade: {avg_grade:.2f}")
        for subject, grade in subjects.items():
            print(f"{subject}: {grade}")
        print()

if __name__=='__main__':
    students = {
        'Alice': {'Math': 90, 'Science': 85, 'English': 88},
        'Bob': {'Math': 70, 'Science': 80, 'English': 72},
        'Charlie': {'Math': 85, 'Science': 92, 'English': 95}
    }

    # Display student summaries
    student_summary(students)
