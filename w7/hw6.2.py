for i in range(1, 8):
    print(f'Shopping for day {i}')
    shopping = True
    daily_total = 0
    
    while shopping:
        grocery = input('Enter grocery name: ')
        price = int(input('Enter price: '))
        daily_total += price

        more = input('More groceries? (y/n): ')
        shopping = more == 'y'
    
    print(f'Total for day #{i}: ${daily_total}')
    print('-' * 20)