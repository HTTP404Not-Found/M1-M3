un1 = int(input())
for x in range(un1-1 , 0,-1):
    print(' ' * x, end='')
    print("*" * (un1 -x))
print("*" * un1)
