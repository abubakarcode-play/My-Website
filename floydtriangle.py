
row = int(input("Enter The Number Of Rows: "))
number = 1
print("Floyds Triangle")
for i in range(1, row+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number = number+1
    print()