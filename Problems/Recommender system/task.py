user_age = abs(int(input()))

if user_age <= 16:
    print("Lion King")
elif 17 <= user_age <= 25:
    print("Trainspotting")
elif 26 <= user_age <= 40:
    print("Matrix")
elif 41 <= user_age <= 60:
    print("Pulp Fiction")
elif user_age > 60:
    print("Breakfast at Tiffany's")
