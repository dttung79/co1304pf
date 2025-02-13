age = int(input('Enter your age: '))
if age < 16:
    print('You are not allowed to join')
elif age >= 18:
    print('You are allowed to join')
else:
    consent = input('Do you have parental consent? (yes/no): ')
    if consent == 'yes':
        print('You are allowed to join')
    else:
        print('You are not allowed to join')