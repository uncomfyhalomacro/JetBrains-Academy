import argparse
import math

parser = argparse.ArgumentParser(description="Calculates anything you want about your credit payments")
parser.add_argument("--type", help="Enter the type of payment.")
parser.add_argument("--payment", type=int, help="Enter the monthly payment")
parser.add_argument("--principal", type=int, help="Enter the principal")
parser.add_argument("--periods", type=int, help="Enter the periods needed to pay your credit.")
parser.add_argument("--interest", type=float, help="Enter your credit interest.")
args = parser.parse_args()


def monthly_interest():  # to simplify the division by 12 months and 100 percentages as the integer is in input
    args.interest = args.interest / 12 / 100


def count_of_months():
    periods_result = math.log(args.payment /
                              (args.payment - args.interest * args.principal), 1 + args.interest)
    if math.ceil(periods_result) < 12:
        print(f"You need {math.ceil(periods_result)} months to repay this credit!")
    elif math.ceil(periods_result) >= 12:
        years = math.ceil(periods_result) // 12
        print("You need {} years and {} months to repay this credit!"
              .format(years, math.ceil(periods_result) - years * 12))
    print(f"Overpayment: {math.ceil(periods_result) * args.payment - args.principal}")


def monthly_payment():
    annuity_payment = (math.ceil(args.principal *
                                 (args.interest * pow(1 + args.interest, args.periods)
                                  / (pow(1 + args.interest, args.periods) - 1))))
    print(f"Your annuity payment - {annuity_payment}!")
    print(f"Overpayment = {annuity_payment * args.periods - args.principal}")


def calculate_principal():
    calculated_principal = (math.floor(args.payment / ((args.interest * pow(1 + args.interest, args.periods))
                                                       / (pow(1 + args.interest, args.periods) - 1))))
    print(f"Your credit principal - {calculated_principal}!")
    print(f"Overpayment: {args.payment * args.periods - calculated_principal}")


def differentiated_payment():
    paid = 0
    for i in range(1, args.periods + 1):
        print("Month {}: paid out {}".format(i, math.ceil(args.principal / args.periods + args.interest *
                                                          (args.principal - (
                                                                      args.principal * (i - 1)) / args.periods))))
        paid += math.ceil((args.principal / args.periods + args.interest *
                           (args.principal - (args.principal * (i - 1)) / args.periods)))
    print("Overpayment = {}".format(paid - args.principal))


def main():
    if (int(args.payment is None) +
        int(args.periods is None) +
        int(args.principal is None) +
        int(args.type is None))\
            >= 2 or args.interest is None:
        print("Incorrect parameters")
    elif args.type == "diff":
        monthly_interest()
        differentiated_payment()
    elif args.type == "annuity":
        monthly_interest()
        if args.payment is None:
            monthly_payment()
        elif args.periods is None:
            count_of_months()
        elif args.principal is None:
            calculate_principal()


if __name__ == "__main__":
    main()
