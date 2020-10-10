number_of_units = abs(int(input()))

if number_of_units == 0:
    print("no army")
elif 1 <= number_of_units <= 9:
    print("few")
elif 10 <= number_of_units <= 49:
    print("pack")
elif 50 <= number_of_units <= 499:
    print("horde")
elif 500 <= number_of_units <= 999:
    print("swarm")
else:
    print("legion")
