def calculate_interest_rate(P, A, t, n):
    temp1 = (A / P)**(1 / (n * t))
    r = n * (temp1 - 1)
    print(f'The interest rate on a loan for {P} ' \
          f'that cost {A} over {t} years is: {r}, ' \
          f'where {P} is the principal amount, ' \
          f'{A} is the total amount paid including both interest and principal (the result of interest.py), ' \
          f'and {t} is the term of the loan in years.')


# In PyCharm, press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to Ethan\'s Interest Rate Calculator!')
    P = input('Total principal amount: ')
    A = input('Total amount paid: ')
    t = input('Term of the loan in years: ')
    n = input('Number of interest payments per year: ')

    # Convert str to proper types
    actual_principal = float(P)
    actual_total_amont = float(A)
    actual_time = int(t)
    actual_number_of_payments = int(n)
    
    calculate_interest_rate(actual_principal, actual_total_amont, actual_time, actual_number_of_payments)
