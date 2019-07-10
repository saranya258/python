rt=int(input())
for ii in range(2,rt):
    if rt%ii==0:
        print("no")
        break
else:
    print("yes")
