num = int(input("Enter your number\n"))
x = num
count = 0
while x!=0:
    x = x//10
    count +=1
print(count)
