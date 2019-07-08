r=int(input())
m=0
i=0
while(r>0):
    i=r%10
    m=m+i
    r=r//10
print(m)
