
#ex1



# x = []
# number = int(input('write the number (integer) '))
# length = int(input('than write the length (integer) '))

# for i in range(1, length + 1):

#     x.append(number * i)

# print(x)



#ex2

word = input('Write a string ')
result = []
for char in word:
    if not result:
       result.append(char)
    elif result and char != result[-1]:
        result.append(char)
    
print(''.join(result))

