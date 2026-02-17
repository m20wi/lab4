#lab4_4
n=int(input('Enter a number: '))
count=0
for i in range(1,n+1):
    if i>50:
        break
    if i%8==0:
        continue
    if i%4==0:
        count+=1
print('Count:',count)