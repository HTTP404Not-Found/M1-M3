un1 =int(input())
for x in range(2 , un1):
    yn = True
    for z in range(2 ,x):
        if x % z == 0:
            yn = False
            break
    if yn:
        print(x)