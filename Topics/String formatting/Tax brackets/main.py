income = int(input())

if income <= 15527:
    percent = 0
    calculated_tax = 0
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income >= 15528 and income < 42708:
    percent = 15
    calculated_tax = int(round(income * 0.15))
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income >= 42708 and income < 132407:
    percent = 25
    calculated_tax = int(round(income * 0.25))
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
else:
    percent = 28
    calculated_tax = int(round(income * 0.28))
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')