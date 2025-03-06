n = int(input('Enter n: '))
FREE_LEVEL = 100

total = 0
frees = 0

for i in range(n):
    product = input('Enter product: ')
    price = int(input('Enter price: '))

    total += price
    if price >= FREE_LEVEL:
        frees += 1

print(f'Total: ${total}')
print(f'There are {frees} products with free ships')