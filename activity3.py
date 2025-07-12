num = int(input("Number:"))


sum = 0



temp = num
while temp > 0:
    digit = temp % 10
    sum+= digit ** 3
    temp //=10


if num == sum:
    print(num , "Is an armstrong value.")
else:
    print(num , "is not  an armstrong value.")