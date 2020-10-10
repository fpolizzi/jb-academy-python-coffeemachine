offset = int(input())

if 14 >= offset >= -12:
    if 10 + offset >= 24:
        print("Wednesday")
    elif 10 + offset <= -1:
        print("Monday")
    else:
        print("Tuesday")
