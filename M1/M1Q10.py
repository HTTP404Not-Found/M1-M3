text = input()
char1 = input()
char2 = input()

for x in text:
    if x == char1:
        print(char2,end='')
    else:
        print(x,end='')
        
print('\n')