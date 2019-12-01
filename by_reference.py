#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program rounds decimals


import math


def round_off(total):
    # rounds off
    total[0] = total[0] * 10**total[1] + 0.5
    total[0] = int(total[0])
    total[0] = float(total[0])
    total[0] = total[0]/(10**total[1])


def main():
    # calls other functions
    # get input
    total = []
    while True:
        number_as_string = input("Enter A Number: ")
        decimal_string = input("Insert how many Decimal Places to Round to: ")
        print()

        try:
            number = float(number_as_string)
            decimal = int(decimal_string)

            total.append(number)
            total.append(decimal)

            round_off(total)

            print(total[0])
            break

        except(ValueError):
            print("Not a valid number input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
