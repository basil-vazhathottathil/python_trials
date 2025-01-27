import os

def add_student(name, grade):
    with open('student_grade.txt', 'a') as file:
        file.write(f"{name} \t {grade}\n")

def display_grades():
    if os.path.exists('student_grade.txt'):
        os.startfile('student_grade.txt')


def calculate_average(total_grade, count):
    avg_grade = total_grade / count
    return avg_grade

def filter_students(filter, student):
    if student['grade'] >= filter:
        with open('passed_students.txt', 'a') as file:
            file.write(f"{student['name']} \t {student['grade']}\n")

def main():
    # Clear files at the start
    open('student_grade.txt', 'w').close()
    open('passed_students.txt', 'w').close()
    with open('student_grade.txt','w') as file:
        file.write('NAME \t GAME\n')

    with open('passed_students.txt','w') as file:
        file.write('NAME \t GAME\n')

    count = int(input('Enter the total number of students: '))
    filter_grade = int(input('Enter the pass grade: '))
    total_grade = 0

    for _ in range(count):
        name = input('Enter the full name of the student: ')
        grade = int(input('Enter the grade: '))
        total_grade += grade

        student = {'name': name, 'grade': grade}
        add_student(name, grade)

        # Check and filter students
        filter_students(filter_grade, student)

    # View grades file
    view_grades = input('Do you want to view the grade file (y or n)? ')
    if view_grades.lower() == 'y':
        display_grades()

    # View average grade
    view_avg = input('Do you want to view the average grade (y or n)? ')
    if view_avg.lower() == 'y':
        print(f"The average grade is: {calculate_average(total_grade, count)}")

    # View passed students
    view_passed = input('Do you want to see the list of passed students (y or n)? ')
    if view_passed.lower() == 'y':
        if os.path.exists('passed_students.txt'):
            os.startfile('passed_students.txt')

main()