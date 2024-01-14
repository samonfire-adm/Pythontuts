user_data = int(input("Enter the year to check whether the year is leap or not "))

if user_data % 4 == 0:
    print(f"{user_data} is a leap year")
else:
    print(f"{user_data} is not a leap year")
    