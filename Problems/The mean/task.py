def mean_integer():
    my_sum = 0
    counter = 0
    while True:

        num = input()

        if num == '.':
            break

        counter = counter + 1
        my_sum = my_sum + int(num)

    print(my_sum / counter)


mean_integer()
