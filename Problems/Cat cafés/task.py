cafe = " "
result_cafe = " "
maximum = 0

while cafe != "MEOW":
    cafe = str(input())

    if cafe == "MEOW":
        break

    input_split = cafe.split()

    if int(input_split[1]) > maximum:
        maximum = int(input_split[1])
        result_cafe = str(input_split[0])

print(result_cafe)
