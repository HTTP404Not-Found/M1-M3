un1 = int(input())
total = 1
for x in range(1 , un1+1):
    total = total * x
    
c = 0
total = str(total)
for x in range(len(total)-1,0,-1):
    if total[x] =='0':
        c = c+1
    else:
        break

print(c)