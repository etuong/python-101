def print_due_date(month, day, year, hour, minute):
    print(f'Module 1 Assignment is due on {month}/{day}/{year} at {hour}:{minute} EST.')


if __name__ == '__main__':
    print('When is your assignment due? ')
    month = input('Month (MM)? ')
    day = input('Day (DD)? ')
    year = input('Year (YYYY)? ')
    hour = input('Hour (HH)? ')
    minute = input('Minute (mm)? ')
    print_due_date(month, day, year, hour, minute)
