# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class RouletteNumbers:
    def __init__(self, t_number, spin_number, color, evenodd, pay):
        self.turn_number = t_number
        self.spin = spin_number
        self.color = color
        self.evenodd = evenodd
        self.pay = pay


def winning_catagory(s_num):
    if s_num < 0 or s_num > 37:
        print("error, spin number out of range.")
        return
    if s_num == 0 or s_num == 37:
        num_col = "Green"
        num_eo = "Neutral"
        # break out
        return num_col, num_eo
    if (s_num % 2) == 0:
        num_eo = "Even"
        num_col = "Neutral"
        if s_num in range(1, 11):
            num_col = "Black"
        if s_num in range(11, 19):
            num_col = "Red"
        if s_num in range(19, 29):
            num_col = "Black"
        if s_num in range(29, 37):
            num_col = "Red"
        return num_col, num_eo
    if (s_num % 2) == 1:
        num_eo = "Odd"
        num_col = "Neutral"
        if s_num in range(1, 11):
            num_col = "Red"
        if s_num in range(11, 19):
            num_col = "Black"
        if s_num in range(19, 29):
            num_col = "Red"
        if s_num in range(29, 37):
            num_col = "Black"
        return num_col, num_eo


def spinwheel(turn_number):
    # increase turn number and store
    turn_number = turn_number + 1
    spin_number = random.randrange(0, 38, 1)
    y = winning_catagory(spin_number)
    return turn_number, spin_number, y[0], y[1]


def maxvalue(money, most_money, tn, hi_tn):
    # keeps track of money value and which turn number
    if money <= most_money:
        return most_money, hi_tn
    if money > most_money:
        most_money = money
        hi_tn = tn
        return most_money, hi_tn


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # user defined variables
    bet_col = "Black"
    bet_eo = "Even"
    cash = 1000
    ogbet = 100
    turns = 100

    # set keeping
    turn_number = 0
    bet_amount = ogbet
    maxmoney = cash
    maxmoneyturn = 0

    while turn_number < turns:
        x = spinwheel(turn_number)
        new_cash = cash - bet_amount
        print(x)
        turn_number = x[0]
        payout = False

        if x[2] == bet_col:
            payout = True
            new_cash = cash + bet_amount
            bet_amount = ogbet

            maxes = maxvalue(new_cash, maxmoney, turn_number, maxmoneyturn)
            maxmoney = maxes[0]
            maxmoneyturn = maxes[1]

            print(f"Winner. You made {bet_amount}.  Your total is now {new_cash}.")
            print(f"The next bet is for {bet_amount}.\n")
        if payout == False:
            print(f"Loser.  You lost {bet_amount}.  Your total is now {new_cash}.")
            bet_amount = bet_amount*2
            if bet_amount > new_cash:
                bet_amount = new_cash
            print(f"The next bet is for {bet_amount}.\n")

        cash = new_cash

        if new_cash < 1:
            print(f"You went bankrupt in {turn_number} turns.")
            print(f"The most money you had was {maxmoney} at turn number {maxmoneyturn}.")
            turn_number = turns

        n1 = RouletteNumbers(x[0], x[1], x[2], x[3], payout)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
