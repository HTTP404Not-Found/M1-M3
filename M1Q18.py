un1 = int(input())
if un1 < -1:
    un1 = 3 * un1 ** 2
    if un1 <= 1:
        un1 = un1 ** 3 + 3 * un1 -3
    else:
        un1 = 2 * un1 + 3
        
print(un1 )