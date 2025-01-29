from datetime import datetime

from entry import Entry


def main():
    """
    Main function to run the application.
    :return: None
    """
    accounting = init_accounts()
    add_entries(accounting)
    show_balance(accounting)


def init_accounts():
    
    return {'Inga':[],'Hans':[],'Samuel':[]}


def add_entries(accounts):
    end = ''
    while end != 'y':
        name = input('Benutzer:')
        accounts[name].append(read_entry())
        end = input('Beenden? (y/N)')


def read_entry():
    start = read_datetime('Start')
    end = read_datetime('End')
    free = read_datetime('Free')
    energy = read_float('Energy')
    return Entry(start,end,free,energy)



def show_balance(accounts):
    for name, entries in accounts.items():
        print(f'Abrechnung für {name}')
        total = 0
        for entry in entries:
            total += entry.cost
            print(f'  - {entry.start:%d.%m.%Y %H:%M}\tCHF {entry.cost:.2f}')
        print(f'{"Total:":<20}\tCHF {total:.2f}')


def read_float(prompt):
    min_value = 0
    while True:
        try:
            zahl = float(input(prompt))
        except ValueError:
            print('Geben Sie eine positive Zahl ein')
        else:
            if zahl < min_value:
                print(f'Geben Sie eine positive Zahl ein')
            else:
                return zahl


def read_datetime(prompt):
    while True:
        try:
            date_input = input(prompt)
            date_time = datetime.strptime(date_input, '%d.%m.%Y %H:%M')
            return date_time
        except ValueError:
            print('Geben Sie ein gültiges Datum/Uhrzeit ein')


if __name__ == '__main__':
    main()
