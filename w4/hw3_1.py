# defensive programing, check if age is valid

age = int(input('Enter your age: '))
# defense
if age <= 0:
    print('Invalid age!')
# attack
else:
    if age < 12:
        print('Children price: $5')
    elif age < 18:
        print('Teenager price: $7')
    elif age < 65:
        print('Adult price: $12')
    else:
        print('Senior price: $8')