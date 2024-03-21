# print('Hello')

import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_counr = {"A": 2, "B": 4, "C": 6, "D": 8}



def get_slot_machine_spin(rows,cols,symbols):
    
    
    
    
    
    
    
    
def deposit():
    while True:
        amount = input("What Would you like to deposit ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be Greater than zero ")
        else:
            print("Please enter a number ")

    return amount


def get_number_of_line():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid Number of Lines ")
        else:
            print("Please enter a number ")

    return lines


def get_bet():
    while True:
        amount = input("What Would you like to bet On  each Line")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be Between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number ")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not enough to bet that amount , your current balance is ${balance} "
            )
        else:
            break
    print(
        f"You are Bettig ${bet} on {lines} lines.Total balance is equel to {total_bet} "
    )


main()
