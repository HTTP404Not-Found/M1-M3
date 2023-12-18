un1 = int(input())
a = list()
a=[]
for x in range(1, un1):
    for y in range(1, un1):
        for z in range(1,un1):
            if x**2 + y**2 == z **2 and z+x+y <=30 and x not in a:
                a = a+[x,y]
                print(str(x) + "    " + str(y)+"    "+ str(z))