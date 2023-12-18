un1 = int(input())
for x in range(1,un1+1):
    for y in range(0 , x):
        print("*",end='')
        if y == x-1:
            print()