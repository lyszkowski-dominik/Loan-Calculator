from math import log
from math import ceil
from math import floor

'''loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'
'''

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
        print("It will take %d months to repay the loan"% months )
    else:
        print("It will take %d months to repay the loan"% (months + 1) )

elif option == 'mp':
    loan_principal = int(input("Enter the loan principal: "))
    months = int(input("Enter the number of months: "))
    monthly_payment = loan_principal / months
    if monthly_payment % 2 == 0:
        print("Your monthly payment = %d" %monthly_payment)
    else:
        monthly_payment += 1
        print(int(monthly_payment))
        print(int(loan_principal - (months - 1) * monthly_payment + 1))
elif option == 'n':
    loan_principal = float(input("Enter the loan principal: "))
    monthly_payment = float(input("Enter the monthly payment: "))
    loan_interest = float(input("Enter the loan interest: "))
    nominal_interest_rate = loan_interest / (12 * 100)
    number_of_months = log(monthly_payment / (monthly_payment - nominal_interest_rate * loan_principal), nominal_interest_rate + 1)
    number_of_months = int(ceil(number_of_months))
    number_of_years = int(number_of_months) / 12
    temporary_years_int = floor(number_of_years)
    rest = ceil((number_of_years - temporary_years_int) * 10)
    if temporary_years_int != 0 and rest != 0:
        print(f'It will take {temporary_years_int} years and {rest} months to repay this loan!')
    elif temporary_years_int == 0:
        print(f'It will take {rest} months to repaay this loan!')
    elif rest == 0:
        print(f'It will take {temporary_years_int} years to repay this loan!')
    else:
        print("Doing calculations failed. There's error somewhere")
elif option == 'a':
    loan_principal = float(input("Enter the loan principal: "))
    number_of_periods = int(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    
else:
    print("Wrong letter")
