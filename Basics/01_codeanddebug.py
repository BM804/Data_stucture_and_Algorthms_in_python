# reverse a number
num = int(input("Enter The number"))
x = num
reverse = 0
while x != 0:
    temp = x%10
    reverse = reverse*10 + temp
    x = x//10
print(reverse)