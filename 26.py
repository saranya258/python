sa=int(input())
at=list(map(int,input().split()[:sa]))
at.sort()
for i in at:
  print(i,end=" ")
