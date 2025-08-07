num = 3
if num > 0:
    print(num, "is a positive number.") 

num = -1
if num > 0:
    print(num, "is a positive number.")

actual_cost=float(input("Please Enter the Actual cost of the product"))
selling_cost=float(input("Please Enter the Selling Price of the product"))

if (selling_cost > actual_cost):
    profit= selling_cost - actual_cost
    print("The profit is", profit)

else:
    print("No profit")

i=int(input("Enter a number:"))
if i < 15:
    print("i is smaller than 15")
    print("I am in if block")
else:
    print("i is greater than 15")
    print("I am in else block")
print("I am not in if and not in else block")
number=int(input("Enter number to check"))
print("Number to be checked:", number)

if number%2==0 :
    print("This is an even number")
else:
    print("This is an odd number")
