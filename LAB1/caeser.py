def Caesar_encrypt(key,text):
    result=""
    for i in range(len(text)):
        variable=text[i]
        if (variable==" "):
            result+=" "
        if(variable.isupper()):
            result+=chr(((ord(variable)-65+key)%26)+65)
        elif (variable.islower()):
            result+=chr(((ord(variable)-97+key)%26)+97)
    return result

def decryption(encrypt,key):
    result=""
    for i in range(len(encrypt)):
        variable=encrypt[i]
        if (variable==" "):
            result+=" "
        if(variable.isupper()):
            result+=chr(((ord(variable)-65-key)%26)+65)
        elif (variable.islower()):
            result+=chr(((ord(variable)-97-key)%26)+97)
    return result


encrypt=Caesar_encrypt(5,"Krisha Pandey")
decrypt=decryption(encrypt,5)
print(encrypt)
print(decrypt)

 
