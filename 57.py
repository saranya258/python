r,r1=map(int,input().split())
m=list(map(int,input().split()[:r]))
k=0
for i in m:
   if(i==r1):
      k=k+1
print(k)
