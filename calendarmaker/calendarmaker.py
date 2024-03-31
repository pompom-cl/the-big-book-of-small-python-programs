import datetime

COL = 3
ROW = 1
WIDTH = 7 * COL + 8
HEIGHT = 5 * ROW + 6

def main():
    date = get_date()
    print_calendar(date, date)


def get_date():
    year, month = 0, 0
    while True:
        year = input("Enter the year for the calendar:\n> ")
        try:
            year = int(year)
        except ValueError:
            pass
        else:
            break
    while True:
        month = input("Enter the month for the calendar:\n> ")
        try:
            month = int(month)
        except ValueError:
            pass
        else:
            break
    return datetime.date(year, month, 1)


def print_calendar(start_date, month):
    while start_date.strftime('%a') != 'Mon':
        start_date -= datetime.timedelta(days=1)

    month_year = month.strftime('%B %Y')
    spaces = ' ' * ((WIDTH - len(month_year)) // 2)
    print(spaces + month_year + spaces)

    day_day = start_date
    for j in range(WIDTH):
        daystring = '.' * ((COL // 2) - 1) + day_day.strftime('%a') + '.' * ((COL // 2) - 1)
        if j % (COL + 1) == 1:
            print(daystring, end='')
            day_day += datetime.timedelta(days=1)
        if j % (COL + 1) == 0:
            print('.', end='')
    print()

    today = start_date
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i % (ROW + 1) == 0 and j % (COL + 1) == 0:
                print('+', end='')
            elif i % (ROW + 1) == 0:
                print('-', end='')
            elif j % (COL + 1) == 0:
                print('|', end='')
            elif i % (ROW + 1) == 1 and j % (COL + 1) == 1:
                print(str(today.day).ljust(COL, ' '), end='')
                today += datetime.timedelta(days=1)
            elif i % (ROW + 1) == 1:
                pass
            else:
                print(' ', end='')
        print()


if __name__ == "__main__":
    main()