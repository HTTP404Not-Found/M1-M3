un1 =int(input())
total = 0
for x in range(1, un1):
    if total + x > un1:
        print(x-1)
        break
    total = total + x
