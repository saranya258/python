g=input()
for i in range(0,len(g)):
   if(g[i].isalpha() and g[i].isdigit()):
    print("No")
else:
  print("Yes")
