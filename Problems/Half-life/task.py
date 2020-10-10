initial = int(input())
final = int(input())

period = 0
while initial >= final:
    initial = initial / 2
    period = period + 1

days = int(period * 12)

print(days)