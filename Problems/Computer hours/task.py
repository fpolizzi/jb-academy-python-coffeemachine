hours_per_day = int(input())

if hours_per_day < 2:
    print("That seems reasonable")
elif hours_per_day < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")
