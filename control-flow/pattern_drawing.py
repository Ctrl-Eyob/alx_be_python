size = int(input("Enter the size of the pattern: "))
row = 0
# Use a while loop to control rows
while row < size:
    # Use a for loop to print stars in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
