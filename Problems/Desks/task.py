class_a = abs(int(input()))
class_b = abs(int(input()))
class_c = abs(int(input()))

desks_a_rest = int(class_a % 2)
desks_a = int(class_a // 2) + desks_a_rest

desks_b_rest = int(class_b % 2)
desks_b = int(class_b // 2) + desks_b_rest

desks_c_rest = int(class_c % 2)
desks_c = int(class_c // 2) + desks_c_rest

sum_desks = desks_a + desks_b + desks_c

print(sum_desks)