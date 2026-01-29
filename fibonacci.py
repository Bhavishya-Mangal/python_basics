def fibonacci_series():
    try:
        n = int(input("Enter the number of terms: "))           # Input from user

        if n <= 0:
            print("Please enter a positive integer.")
        else:
            a, b = 0, 1
            print("Fibonacci Series:")

            for _ in range(n):
                print(a, end=' ')
                a, b = b, a + b
            print()

    except ValueError:
        print("Please enter a valid natural integer.")

fibonacci_series()

# This code generates the Fibonacci series up to 'n' terms as specified by the user.

# Example:
    # Input: 7 → Output: 0 1 1 2 3 5 8
    # Input: 0 → Output: Please enter a positive integer.
    # Input: -4 → Output: Please enter a positive integer.