# Author: Johnny Lu
# Contact: joh@johdev.com
# Copyright: Johnny Lu
# LICENSE: MIT
import argparse
from src.calculatorMode import InteractMode
from src.calculatorMode import CLImode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['annuity', 'diff'], help='the type of payments')
    parser.add_argument('--payment', type=int, help='monthly payment')
    parser.add_argument('--principal', type=int, help='to calculate payment')
    parser.add_argument('--periods', type=int, help='the number of months needed to repay the loan')
    parser.add_argument('--interest', type=float, help='loan interest rate, in % (DO NOT NEED TO TYPE %)')

    args = parser.parse_args()
    if not args.type and not args.payment and not args.principal and not args.periods and not args.interest:
        InteractMode()

    else:
        CLImode(args=args)


if __name__ == '__main__':
    main()
