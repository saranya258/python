nt=int(input())
pt=0
ht=nt
while ht>0:
 digit =ht%10
 pt+= digit ** 3
 ht //=10
if nt==pt:
 print("yes")
else:
 print("no")
