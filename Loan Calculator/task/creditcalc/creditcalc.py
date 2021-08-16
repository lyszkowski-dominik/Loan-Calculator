loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
loan_principal = int(input("Enter the loan principal: "))
print("What do you want to calculate ?")
print('type "m" for number of monthly payments, ')
print('type "p" for the monthly payment')
option = input()

if option == 'm':
    monthly_payment = int(input("Enter monthly payment: "))
    months = int(loan_principal / monthly_payment)
    if months == 1:
        print("It will take 1 month to repay the loan")
    elif months * monthly_payment >= loan_principal:
        print("It will take %d months to repay the loan"% months )
    else:
        print("It will take %d months to repay the loan"% (months + 1) )

elif option == 'p':
    months = int(input("Enter the number of months: "))
    monthly_payment = loan_principal / months
    if monthly_payment % 2 == 0:
        print("Your monthly payment = %d" %monthly_payment)
    else:
        monthly_payment += 1
        print(int(monthly_payment))
        print(int(loan_principal - (months - 1) * monthly_payment + 1))
else:
    print("Wrong letter")
