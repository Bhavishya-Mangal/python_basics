try:
        a = int(input("Enter a number: "))          # Input from user

        if a % 2 == 0:
            print(f"{a} is Even")
        else:
            print(f"{a} is Odd")

except ValueError:
    print("Please enter a valid integer.")

# This code checks if the entered number is even or odd.

# Example:

# Input: 4
# Output: 4 is Even

# Input: 7
# Output: 7 is Odd