def calculate_interest(P, r, t, n):
    A = P*pow(1 + (r / n), n * t)
    interest = A - P
    print(f'Total paid after {t} years: {A}')
    print(f'Interest paid after {t} years: {interest}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to Ethan\'s Interest Calculator!')
    P = input('Total principal amount: ')
    r = input('Interest rate: ')
    t = input('Term of the loan in years: ')
    n = input('Number of interest payments per year: ')
    actual_principal = float(P)
    actual_rate = float(r)
    actual_time = int(t)
    actual_number_of_payments = int(n)
    calculate_interest(actual_principal, actual_rate,
                       actual_time, actual_number_of_payments)
