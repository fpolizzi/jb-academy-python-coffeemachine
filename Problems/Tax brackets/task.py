income = int(input())

if 0 <= income <= 15527:
    tax = 0
elif 15528 <= income <= 42707:
    tax = 15
elif 42708 <= income <= 132406:
    tax = 25
elif income >= 132406:
    tax = 28

if tax != 0:
    calculated_tax = (income * (tax / 100))
else:
    calculated_tax = 0

print('The tax for {income} is {percent}%. That is {calculated_tax} dollars!'.
      format(income=income, percent=tax, calculated_tax=round(calculated_tax)))
