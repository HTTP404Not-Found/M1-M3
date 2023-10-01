text = str(input())
text = list(text)
i = 0
while i < 4:
    text[i] = str((int(text[i]) + 7) % 10 )
    i += 1

t = text[0] 
text [0] = text [2]
text[2] =t

t = text[1]
text [1] = text[3]
text [3] = t

print(''.join(text) , '\n' )