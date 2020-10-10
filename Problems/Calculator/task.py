number_1 = float(input())
number_2 = float(input())
operator = input()

division_by_zero_operators = ['/', 'mod', 'div']

if operator == '+':
    print(number_1 + number_2)
elif operator == '-':
    print(number_1 - number_2)
elif operator == '*':
    print(number_1 * number_2)
elif operator == 'pow':
    print(number_1 ** number_2)
elif operator in division_by_zero_operators and number_2 == 0.0:
    print("Division by 0!")
elif operator == '/':
    print(number_1 / number_2)
elif operator == 'mod':
    print(number_1 % number_2)
elif operator == 'div':
    print(number_1 // number_2)
