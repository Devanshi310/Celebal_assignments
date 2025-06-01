# Printing triangle pattern
def pattern(n):
    for i in range(n):  # Outer loop runs for 'n' rows
        # First inner loop prints 'n - i - 1' spaces before stars
        for j in range(n - i - 1):  # For row i, we want the stars centered by adding spaces to the left
            print(" ", end="")  # Use end="" to print spaces on the same line

        # Second inner loop prints stars
        for j in range(2 * i + 1):  # The number of stars follows the formula '2 * i + 1' (odd numbers)
            print("*", end="")

        # Third inner loop prints trailing spaces
        for j in range(n - i - 1):  # These are optional for visual symmetry; logic is the same as leading spaces
            print(" ", end="")

        print()  # Move to the next line after finishing one row

def main():
    n = int(input("Enter the number of rows: "))
    pattern(n)

if __name__ == "__main__":
    main()