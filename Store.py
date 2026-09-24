##---------------------------Simple Grocery Store-------------------------------##

print("Groceries Items")
print('''
S No.\tItems\t\tQty.\tPrice
\n1:\tPotatoes\t1kg\t80rs
2:\tTomatoes\t1kg\t67rs
3:\tBananas\t\t1dozen\t100rs
4:\tApple\t\t1kg\t50rs
5:\tCauliflower\t1kg\t40rs
''')


list_of_items = ["Potatoes","Tomatoes","Bananas","Apple","Cauliflower"]


cart = []
n = int(input("Enter the no. of items you want to purchase: "))
while n != 0:
    if n < 0:
        print("The items cant be negative.")
        n = int(input("Enter the no. items you want to purchase: "))
        continue

    while n != 0:
        a = int(input("Enter S.No of item which you want to purchase: "))
        if a >= 6 or a-1 < 0:                              # Here I converted my indexing as index[0] is treated as index[1] and as follows
            print("Please select items from the list")
            continue
        while a >= 6 or a-1 < 0:
            a = int(input("Enter items no. to purchase: "))
            continue
        if a >= 6 or a-1 < 0:
            print("Please select items from the list")
            continue
        print(list_of_items[a-1])
        cart.append(list_of_items[a-1])
        n-=1
    print(cart)

    a = input("Do you want to add more (y/n): ")
    if a == "y":
        n = int(input("Enter the no. items you want to purchase: "))
    else:
        n=0


if cart == []:
    print("Please enter a value item number.")
else:
    print(cart)
