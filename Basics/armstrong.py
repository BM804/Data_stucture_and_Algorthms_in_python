while True: #continiously taking input
    num = int(input("Enter the Number ! \n"))
    n = num
    l = len(str(num))
    arm = 0
    while n!=0:
        temp = n%10
        arm += temp**l
        n = n//10
    if arm ==num:
        print("Yes the number is armstrong")
    else:
        print("No !!")