print("Please enter two numbers to swap to string:")
    a = int(input())
    b = int(input())
    a, b = swap_numbers(a, b)
    print(f"The two swapped numbers are: {a} and {b}")

    print("\nPlease enter a number to print it in natural descending order:")
    n = int(input())
    print_descending(n)