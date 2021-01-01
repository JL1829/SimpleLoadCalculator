# Author: Johnny Lu
# Contact: joh@johdev.com
# Copyright: Johnny Lu
# LICENSE: MIT
from .loancalculator import LoanCalculator


def InteractMode():
    calculator = LoanCalculator()
    while True:
        print('\nWhat do you want to calculate?\n'
              'type "n" for number of monthly payments,\n'
              'type "a" for annuity monthly payment amount,\n'
              'type "p" for loan principal:\n'
              'type "d" for differentiated payment\n'
              '\ntype "q" for Exit')

        method = input(">")

        if method == 'n':
            print("Enter the loan principal:")
            calculator.principal = float(input(">"))
            print("Enter the monthly payment:")
            calculator.annuity = int(input(">"))
            print("Enter the loan interest:")
            period, overpayment = calculator.getPeriod(
                interest=float(input(">")))
            year, month = divmod(period, 12)
            if year == 0:
                print(f"It will take {month} months to repay this loan!\n"
                      f"Overpayment = {overpayment}")
            elif year == 1 and month == 0:
                print(f"It will take {year} year to repay this loan!\n"
                      f"Overpayment = {overpayment}")
            elif year > 1 and month == 0:
                print(f"It will take {year} years to repay this loan!\n"
                      f"Overpayment = {overpayment}")
            else:
                print(
                    f"It will take {year} years and {month} months to repay this loan!\n"
                    f"Overpayment = {overpayment}")

        elif method == 'a':
            print("Enter the loan principal:")
            calculator.principal = int(input(">"))
            print("Enter the number of periods:")
            calculator.period = int(input(">"))
            print("Enter the load interest:")
            payment, overpayment = calculator.getAnnuityAmount(
                interest=float(input(">")))
            print(f"Your monthly payment = {payment}!\n"
                  f"Overpayment = {overpayment}")

        elif method == 'p':
            print("Enter the annuity payment:")
            calculator.annuity = float(input(">"))
            print("Enter the number of periods:")
            calculator.period = int(input(">"))
            print("Enter the loan interest:")
            principal, overpayment = calculator.getPrincipal(
                interest=float(input(">")))
            print(f"Your loan principal = {principal}!\n"
                  f"Overpayment = {overpayment}")

        elif method == 'd':
            print('Enter the loan principal:')
            calculator.principal = int(input(">"))
            print('Enter the number of periods:')
            calculator.period = int(input(">"))
            print('Enter the loan interest:')
            differentiated, overpayment = calculator.getDiff(
                interest=float(input(">")))
            for month, payment in enumerate(differentiated):
                print(f"Month: {month + 1}: payment is {payment}")
            print(f"\nOverpayment = {overpayment}")

        elif method == 'q':
            break


def CLImode(args):
    if not args.type:
        print("Incorrect parameters")

    if args.type == 'diff' and args.principal and args.periods and args.interest:
        cal = LoanCalculator()
        cal.principal = args.principal
        cal.period = args.periods
        diff, overpayment = cal.getDiff(interest=args.interest)
        for month, payment in enumerate(diff):
            print(f"Month: {month + 1}: payment is {payment}")
        print(f"\nOverpayment: {overpayment}")
    elif args.type == 'annuity' and args.principal and args.periods and args.interest:
        cal = LoanCalculator()
        cal.principal = args.principal
        cal.period = args.periods
        annuity, overpayment = cal.getAnnuityAmount(interest=args.interest)
        print(f"Your annuity payment = {annuity}\n"
              f"Overpayment = {overpayment}")
    elif args.type == 'annuity' and args.payment and args.periods and args.interest:
        cal = LoanCalculator()
        cal.annuity = args.payment
        cal.period = args.periods
        principal, overpayment = cal.getPrincipal(interest=args.interest)
        print(f"Your loan principal = {principal}!\n"
              f"Overpayment = {overpayment}")
    elif args.type == 'annuity' and args.principal and args.payment and args.interest:
        cal = LoanCalculator()
        cal.principal = args.principal
        cal.annuity = args.payment
        periods, overpayment = cal.getPeriod(interest=args.interest)
        year, month = divmod(periods, 12)
        if year == 0:
            print(f"It will take {month} months to repay this loan!\n"
                  f"Overpayment = {overpayment}")
        elif year == 1 and month == 0:
            print(f"It will take {year} year to repay this loan!\n"
                  f"Overpayment = {overpayment}")
        elif year > 1 and month == 0:
            print(f"It will take {year} years to repay this loan!\n"
                  f"Overpayment = {overpayment}")
        else:
            print(
                f"It will take {year} years and {month} months to repay this loan!\n"
                f"Overpayment = {overpayment}")

    else:
        print("Incorrect parameters.")
