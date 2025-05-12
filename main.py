import sys




def main():
    one_check()
    interest_with_pay()
    try_again()

def one_check():
    try:
        total_due = float(input("What is the Net total? "))
        number_of_payments = int(input("In how many payments? "))
    except ValueError:
        print("Oh no! That's not a valid value. Try again...")
    else:
        amount_due = total_due / number_of_payments
        print("The net pay per payment due and before interest is: ${}".format(amount_due))

# interest rate function
def interest_with_pay():
    try:
        first_payment = float(input("How much do the user owe? "))
        interest_rate = float(input("What is the interest rate per partial payment? "))
    except ValueError:
        print("Oh no! That's not a valid value. Try again...")
    else:
        n = first_payment / interest_rate
        r = n + first_payment
        amount_with_interest = r
        print("The amount with interest per payment after due date is: ${}".format(r))

def try_again():
    while True:
        x = input("Try again? ").lower()
        if x == "yes":
            one_check()
        else:
            sys.exit()


if __name__=="__main__":
    main()
