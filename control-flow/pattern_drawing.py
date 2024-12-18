#Prompt User for Pattern Size:
size = int(input("Enter the size of the pattern:"))

row = 0

#Draw the pattern
while row < size:
    for col in range(size):
        print("*", end="")

    print()
    row += 1
