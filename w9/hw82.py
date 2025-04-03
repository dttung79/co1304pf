def enter_customer_tickets(customers, tickets):
    n = len(customers)
    for i in range(n):
        customers[i] = input(f'Enter name of customer {i+1}: ')
        tickets[i] = int(input(f'Enter ticket number of customer {i+1}: '))

def print_customers(customers, tickets):
    n = len(customers)
    for i in range(n):
        print(f'{i+1}. {customers[i]}: {tickets[i]}')

def calculate_total_tickets(tickets):
    total = 0
    for t in tickets:
        total += t
    
    return total

def main():
    n = int(input('Enter number of customers: '))
    customers = [None] * n # create n elements of None
    tickets = [None] * n
    enter_customer_tickets(customers, tickets)
    print_customers(customers, tickets)
    print(f'Total tickets sold: {calculate_total_tickets(tickets)}')

### Main program ###
main()