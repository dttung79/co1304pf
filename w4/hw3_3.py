amount = int(input("Enter the amount spent: "))
final_price = amount
if amount < 50:
    print("No discount")
elif amount <= 100:
    print("Discount 10%")
    final_price *= 0.9 # shortcut for final_price = final_price * 0.9
else:
    print("Discount 20%")
    final_price *= 0.8

print("Final price: $", final_price)