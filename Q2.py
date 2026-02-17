# lab4_Q2
number=int(input('Enter a number: '))
for i in range(1,14):
    mul=number*i
    if mul>50:
        break
    if mul%3==0:
        continue
    print(number,'*',i,'=',mul)