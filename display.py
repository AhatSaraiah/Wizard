from operator import itemgetter
from colorama import Fore, Style
from tabulate import tabulate

reset=False

def display_summary(details):
    global rest
    show_phase(1, details)
    show_phase(2, details)
    show_phase(3, details)
    show_phase(4, details)

    rest_button=input(f"{Fore.YELLOW} \nenter 1 if you want to rest:")
    if rest_button=="1":
        rest_data(details)
    else:
        print("Invalid number")


def show_phase(num_phase,details):
    phase_functions = {
        1: lambda: print_items(1,details, 0, 3),
        2: lambda: print_items(2,details, 3, 6),
        3: lambda: print_items(3,details, 6, 8),
        4: lambda: print_items(4,details, 8, 11)
    }
    phase_functions.get(num_phase, lambda: print("Invalid phase number"))()


def print_items(num_phase,details, start, end):
    table_data = []
    for key, value in list(details.items())[start:end]:
        table_data.append([f'{Fore.BLUE}{key}:{Fore.LIGHTRED_EX}', value])

    table = tabulate(table_data, headers=["Item", "Value"], tablefmt="grid", colalign=("left", "right"))
    print(f'{Fore.GREEN}Phase {num_phase} items:\n')
    print(table)
    print(Style.RESET_ALL)

def get_reset():
    return reset

def rest_data(details):
    global rest
    for k,v in details.items():
        details[k]=None
    rest=True




def show_wizards_history(wizard):
    if not wizard.users:
        print("No wizards completed yet.")
        return

    headers = list(wizard.users[0].keys())
    wizards_data = [list(user.values()) for user in wizard.users]

    print(tabulate(wizards_data, headers=headers))

    while True:
        choice = input("\n\n\nSort by column: (1) Name (2) Email (3) Birth Date (4) City (5) Street "
                            "(6) Number (7) Social Media (8) Hobbies (9) Happy (10) Skydiving (11) One Dollar (0) Cancel: ")
        if choice == "0":
            break
        if choice.isdigit() and 1 <= int(choice) <= len(headers):
            column_index = int(choice) - 1
            sorted_wizards = sorted(wizard.users, key=itemgetter(headers[column_index]))
            print(tabulate([list(user.values()) for user in sorted_wizards], headers=headers))
        else:
            print("Invalid choice. Please enter a number between 1 and 11 or '0' to cancel.")

