a = 10
b = 12
c = 0
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleas one number has boolean value as False")

a=10
b=-10
c=0
if a>0 or b>0:
    print("Either of the number is greator than O")
else:
    print("No number is greator than 0")
if b>0 or c>0:
    print("Either of the number is greator than O")
else:
    print("No number is greator than 0")

a=10
b=12
c=12
print("a != b")
print("b != c")

a="python"
b="coding"
if a != b :
    print(a, 'and', b, "are different.")

a=4
b=5
if (a == 1) != ( b == 5):
    print("Hello")

a=int(input("Enter a number"))
if a%2 != 0 :
    print(a, "Number is not even number")

height = float(input("Enter your height"))
weight = float(input("Enter your weight"))
BMI = weight / (height/100)**2 
print("Your BMI is", BMI)
if BMI <= 18.4:
    print("You are under weight.")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are OverWieght")
elif BMI <= 34.9:
    print("You are Severely overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")