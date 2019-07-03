fan,msd=map(int,input().split())
for nu in range(fan,msd):
  temp=nu
  s=0
  while tem>0:
      dig=tem%10
      s=s+dig**3
      tem=tem//10
      if s==nu:
           print (nu, end=' ')
