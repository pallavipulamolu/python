num = int(input("Enter a number: "))
s = num
sum1 = 0
b = len(str(num))
while num != 0:
    r = num%10
    sum1 += (r**b)
    num = num//10
if s == sum1:
    print("The given number armstrong number")
else:
    print("The given number is not armstrong number")
