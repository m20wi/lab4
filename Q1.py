#lab4_Q1
totall=0
for i in range(10):
    number=(int(input("enter 10 number:")))
    if number==0:
        break
    if number<0:
        continue
    if number>0 and number % 2==0:
        totall+=number
print('The final sum is:',totall)


