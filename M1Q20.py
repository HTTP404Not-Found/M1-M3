un1 = int(input())
x1 = int(input())
x2 = int(input())
x3 = int(input())

un2 = x1 *15 + x2 * 20 +x3 *30
un3 = (un1 - un2)
if un2 > un1:
    print(0)
else:
    
    x1=un3 // 50
    un3 =  un3 - (un3 // 50)*50
    x2=un3 // 5
    un3 =  un3 - (un3 // 5)*5
    x3=un3 // 1
    un3 =  un3 - un3 // 1
    
    print(x3,'\n',x2,'\n',x1,'\n')
    
    
    
    
    