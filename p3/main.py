
n1 = int(input("Enter the first number \n"))
n2 = int(input("Enter the second number \n"))
n3 = int(input("Enter the third number \n"))

if n1>=n2 and n1>=n3:
    max_num = n1
elif n2>=n1 and n2>= n3:
    max_num = n2
else:
    max_num = n3

print(f"{max_num} is greatest among {n1}, {n2}, {n3}")