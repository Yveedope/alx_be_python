#Prompt user for a number
number = input("Enter a number to see its multiplication table:")

#Generate and print multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")