# #ex1

# user_str = input('Write a string of words (it will be separated by commas)  >> ')
# split_str = user_str.split(',')
# split_str = [word.strip() for word in user_str.split(',')]
# split_str.sort()
# x = ','.join(split_str)

# print(x)


#ex2

def takes_str():
    sentence =(input('Write your sentence >> '))
    words = sentence.split()
    longest = ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(takes_str())
   
