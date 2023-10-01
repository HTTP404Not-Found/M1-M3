text = str(input())
text = str((int(text) + 7) % 10)

print(text , '\n' )
t = text[0] 
text [0] = text [2]
text [2] = t

print(text , '\n' )