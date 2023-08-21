def getCipher(text, rails):
    ciphertext = ""
    length_row = 0
    extra_char = 0

    
    for i in range(rails):
        ctext = ""
        for j in range(i, len(text), rails):
            ctext += text[j]

        if i == 0:
            length_row = len(ctext) 
        if i != 0 and len(ctext) < length_row:
            ctext += "X"  # adding extra alphabet
            extra_char += 1

        ciphertext += ctext  

        print(ctext)

    return ciphertext, extra_char


# Decipher
def getDecipher(text, rails):
    deciphertext = ""
    length = int(len(text) / rails)

  
    for i in range(0, length):
        # Inner loop runs though the rows of columns
        for j in range(0, rails):
            deciphertext += text[length * j + i]  

    return deciphertext


# Input
plain_text = input("Enter the plain text: ").upper().replace(" ", "")
rails = int(input("Enter the rails: "))

# Ciphered Text
cipher_text, extra = getCipher(plain_text, rails)
print("Ciphered Text: " + cipher_text)

# Deciphered Text
decipher_text = getDecipher(cipher_text, rails)
print("Deciphered Text: " + decipher_text[:len(cipher_text)-extra])
