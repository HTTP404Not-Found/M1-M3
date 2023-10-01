#un1 = input()
#un1 = un1[:3] + '1' + un1[4:]  # Create a new string with the fourth character replaced by '1'
#print(un1)

#un1 = input()
#un1_list = list(un1)  # Convert the string to a list of characters
#un1_list[3] = "1"    # Replace the character at index 3 with "1"
#modified_un1 = ''.join(un1_list)  # Convert the list back to a string
#print(modified_un1)

un1= list(input())
un1[2] = "1"
un2 = ''.join(un1)
print(un2)