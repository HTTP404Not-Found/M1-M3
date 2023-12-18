un1 = int(input())
x = 1
y =0
while True:
    x = x + y
    y +=1
    print(x,"   ", end='')
    if x > un1 :
        break
print()
for x in range(1 , un1+2):
    for y in range(0 , x):
        print(x, "  ",end='')