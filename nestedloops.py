string = input("Please Enter Your Word:")
char = input("Please enter your Character:")
i = 0
count = 0
while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1
print("The Total Number of Times", char, "has occured = ", count)