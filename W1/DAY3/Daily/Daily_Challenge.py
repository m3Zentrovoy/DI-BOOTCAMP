
# Challenge 1

dictonary = {}
word = input("Enter a word ")

for index, char in enumerate(word):
    if char in dictonary:
     dictonary[char].append(index)
    else:
        dictonary[char] = [index]

print(dictonary)


# Challenge 2

items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
wallet = int(wallet.replace('$',''))
new_list = []
for name, val in items_purchase.items():

    val = int(val.replace('$', '').replace(',',''))
    if val <= wallet:
        wallet = (wallet - val)
        new_list.append(name)
if val > wallet:
    print('Nothing')
else:
    print(sorted(new_list))

