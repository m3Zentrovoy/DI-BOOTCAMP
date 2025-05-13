


cypher_text = []
request =input("You wants to encrypt or decrypt text >> ")
if request == "encrypt":
    text_enc = (input('Write your text for encryption >> '))
    for letter in text_enc:
        cypher_text += chr(ord(letter) + 3)

elif request == "decrypt":
    text_dec = (input('Write your text for encryption >> '))
    for letter in text_dec:
        cypher_text += chr(ord(letter) - 3)

print(cypher_text)
