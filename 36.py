san=input()
sat=0
for i in range(len(san)):
  if(san[i].isdigit() or san[i].isalpha() or san[i]==(" ")):
    continue
  else:
    sat+=1
print(sat)
