def enter_fruits(fruits):
    n = len(fruits)
    for i in range(n):
        fruits[i] = input(f'Enter fruit {i+1}: ')

def print_fruits(fruits):
    n = len(fruits)
    for i in range(n):
        print(f'{i+1}. {fruits[i]}')

def main():
    n = int(input('Enter number of fruits: '))
    # init a list of None values
    fruits = [None] * n
    # call the function to enter fruits
    enter_fruits(fruits)
    # call the function to print fruits
    print_fruits(fruits)

### Main program ###
main()