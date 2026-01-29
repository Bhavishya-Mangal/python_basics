def calculate_factorial():

    try:
        a = int(input("Enter a number: "))      # Input from user
 
        if a < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            fact = 1
            for i in range(1, a + 1):
                fact *= i
            print(f"The factorial of {a} is {fact}")
    except ValueError:
        print("Please enter a valid natural number.")
    
calculate_factorial()

# This code calculates the factorial of a non-negative integer entered by the user.

# Example:
    # Input: 5 → Output: The factorial of 5 is 120
    # Input: -3 → Output: Factorial is not defined for negative numbers.