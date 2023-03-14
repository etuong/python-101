def get_sum(n):
    digitSum = 0
    while n != 0:
        digitSum = digitSum + (n % 10)
        n = n // 10
    return digitSum


if __name__ == '__main__':
    number = input("Credit Card Number? : ")

    # Check that char is a digit
    if not number.isdecimal():
        print("Please only enter digits!\n")
        exit()

    # Create a variable to keep track of a running total that is initially 0
    running_total = 0

    # For every other digit beginning with the last (N, N-2, N-4, and so on),
    for even_digit_str in number[len(number)-1::-2]:
        # Convert string to int on the digit
        even_digit = int(even_digit_str)

        # Multiply it by 2
        even_digit = even_digit * 2

        # If the result is a 1-digit number, add it to the running total
        if even_digit < 10:
            running_total += even_digit
        else:  # If the result is a 2-digit number, add the digits together
            digitSum = get_sum(even_digit)
            # Then add that number to the running total
            running_total += digitSum

    # For all of the digits in-between
    for odd_digit_str in number[len(number)-2::-2]:
        # Just add them directly to the running total
        odd_digit = int(odd_digit_str)
        running_total += odd_digit

    check_digit = 10 - running_total % 10
    print(f"The valid credit card number is: {number}{check_digit} and the newly computed check digit is: {check_digit}")
