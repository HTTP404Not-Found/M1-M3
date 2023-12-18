un1 =int(input())
total = un1
while un1 // 3 >0 :
    new = un1 // 3
    total = total  + new
    un1 = un1 + new - (3 * new)
    
    
print(total)