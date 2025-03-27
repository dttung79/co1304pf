def enter_students(students):
    n = len(students)
    for i in range(n):
        students[i] = input(f'Enter name of student {i+1}: ')

def enter_grades(grades):
    n = len(grades)
    for i in range(n):
        grades[i] = int(input(f'Enter grade of student {i+1}: '))
    
def print_students(students, grades):
    n = len(students)
    for i in range(n):
        print(f'{i+1}. {students[i]}: {grades[i]}')

def avg_grades(grades):
    n = len(grades)
    s = 0
    for g in grades:
        s += g
    return s / n

def main():
    n = int(input('Enter number of students: '))
    students = [None] * n # create n elements of None
    grades = [None] * n
    enter_students(students)
    enter_grades(grades)
    print_students(students, grades)
    print(f'Average grade: {avg_grades(grades)}')

### Main program ###
main()