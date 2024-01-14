def max_num(n1, n2, n3 ):
    return max(n1,n2,n3)

n1 = int(input("Enter the first number \n"))
n2 = int(input("Enter the second number \n"))
n3 = int(input("Enter the third number \n"))

max_number =max_num(n1,n2,n3)
print(f"{max_number} is greatest among {n1}, {n2}, {n3}") 