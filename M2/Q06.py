un1 = int(input())
YN = 'YES'
for x in range(2,un1):
    if un1 % x == 0:
        YN = 'NO'
        break
if YN == 'YES':
    print("YES")
else:
    print("NO")