un1 = int(input())
sum = 0
for x in range(1, un1+1):
    if x % 3 == 0 :
        sum = x + sum
print(sum)