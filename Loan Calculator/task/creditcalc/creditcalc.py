from math import log
from math import ceil
from math import floor

# write your code here
print("What do you want to calculate ?")
print('type "m" for number of monthly payments, ')
print('type "mp" for the monthly payment')
print('type "n" for number of monthly payments')
print('type "a" for annuity monthly payment amount')
print('type "p" for loan principal')


option = input()

if option == 'm':
    loan_principal = int(input("Enter the loan principal: "))
    monthly_payment = int(input("Enter monthly payment: "))
    months = int(loan_principal / monthly_payment)
    if months == 1:
        print("It will take 1 month to repay the loan")
    elif months * monthly_payment >= loan_principal:
        print("It will take %d months to repay the loan" % months)
    else:
        print("It will take %d months to repay the loan" % (months + 1))

elif option == 'mp':
    loan_principal = int(input("Enter the loan principal: "))
    months = int(input("Enter the number of months: "))
    monthly_payment = loan_principal / months
    if monthly_payment % 2 == 0:
        print("Your monthly payment = %d" % monthly_payment)
    else:
        monthly_payment += 1
        print(int(monthly_payment))
        print(int(loan_principal - (months - 1) * monthly_payment + 1))
elif option == 'n':
    loan_principal = float(input("Enter the loan principal: "))
    monthly_payment = float(input("Enter the monthly payment: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / (12 * 100)
    number_of_months = log(monthly_payment /
                           (monthly_payment - i * loan_principal), i + 1)
    print(number_of_months)
    number_of_months = int(ceil(number_of_months))
    number_of_years = int(number_of_months) / 12
    temporary_years_int = floor(number_of_years)
    rest = number_of_months - (temporary_years_int * 12)
    if number_of_months > 12:
        print(f'It will take {temporary_years_int} years and {rest} months to repay this loan!')
    elif number_of_months < 12:
        print(f'It will take {rest} months to repay this loan!')
    elif rest == 0 or number_of_months == 12:
        print(f'It will take {temporary_years_int} years to repay this loan!')
    else:
        print("Doing calculations failed. There's error somewhere")
elif option == 'a':
    loan_principal = float(input("Enter the loan principal: "))
    number_of_periods = int(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / (12 * 100)
    annuity = loan_principal * \
              ((i * pow((1 + i), number_of_periods)) /
         (pow((1 + i), number_of_periods) - 1))
    annuity = ceil(annuity)
    print(f'Your monthly payment = {annuity}!')
elif option == 'p':
    annuity_payment = float(input("Enter your annuity payment: "))
    number_of_periods = int(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / (12 * 100)
    loan_principal = annuity_payment / ((i * pow((1 + i), number_of_periods)) /
                                        (pow((1 + i), number_of_periods) - 1))
    loan_principal = int(loan_principal)
    print(loan_principal)
else:
    print("Wrong letter")
