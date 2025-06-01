# Function to print a lower right-angled triangle pattern of stars
def pattern(n):
    # Outer loop for each row
    for i in range(n):
        # Inner loop to print stars
        # For row 'i', print (i + 1) stars
        for j in range(i + 1):
            print("*", end="")  # Print star without moving to next line
        print()  # Move to the next line after each row

def main():
    n = int(input("Enter the number of rows: "))
    pattern(n)

if __name__ == "__main__":
    main()