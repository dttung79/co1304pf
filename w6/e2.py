n = int(input('Enter n: '))
total = 0
fails = 0

for i in range(n):
    name = input('Enter student name: ')
    grade = int(input('Enter grade: '))
    
    total += grade
    if grade < 40:
        fails += 1

avg = total / n

print(f'Average grade: {avg:.2f}')
print(f'There are {fails} students who failed')