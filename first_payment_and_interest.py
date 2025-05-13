def return_first_payment(first_payment, interest_rate):
    if interest_rate < 1:
        raise ValueError("Not less than 1 percent interest")
    return first_payment/interest_rate+first_payment

try:
    first_payment = float(input("What is the amount of the first payment? "))
    interest_rate = float(input("What is the interest rate? "))
    amount_due = return_first_payment(first_payment, interest_rate)
except ValueError as err:
    print("Not a valid value. Try again...")
    print("({})".format(err))
else:
    print("The total due is: ${}".format(amount_due))
