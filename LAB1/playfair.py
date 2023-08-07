def generate_playfair_square(key):

    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key + alphabet

   
    key = "".join(dict.fromkeys(key))

    playfair_square = [['' for _ in range(5)] for _ in range(5)]
    row, col = 0, 0

    for letter in key:
        if col == 5:
            col = 0
            row += 1
        playfair_square[row][col] = letter
        col += 1

    return playfair_square

def find_letter_coordinates(square, letter):
  
    for i in range(5):
        for j in range(5):
            if square[i][j] == letter:
                return i, j

def encrypt_pair(square, pair):
    
    a, b = pair[0], pair[1]
    row_a, col_a = find_letter_coordinates(square, a)
    row_b, col_b = find_letter_coordinates(square, b)

    if row_a == row_b:
        return square[row_a][(col_a + 1) % 5] + square[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return square[(row_a + 1) % 5][col_a] + square[(row_b + 1) % 5][col_b]
    else:
        return square[row_a][col_b] + square[row_b][col_a]

def encrypt(message, square):
   
    message = message.replace(" ", "").upper()

    
    i = 0
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message = message[:i + 1] + 'X' + message[i + 1:]
        i += 2

    
    if len(message) % 2 != 0:
        message += 'X'

    encrypted_message = ""
    for i in range(0, len(message), 2):
        pair = message[i:i + 2]
        encrypted_message += encrypt_pair(square, pair)

    return encrypted_message

def decrypt_pair(square, pair):
    
    a, b = pair[0], pair[1]
    row_a, col_a = find_letter_coordinates(square, a)
    row_b, col_b = find_letter_coordinates(square, b)

    if row_a == row_b:
        return square[row_a][(col_a - 1) % 5] + square[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return square[(row_a - 1) % 5][col_a] + square[(row_b - 1) % 5][col_b]
    else:
        return square[row_a][col_b] + square[row_b][col_a]

def decrypt(encrypted_message, square):
  
    encrypted_message = encrypted_message.replace(" ", "").upper()

    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        pair = encrypted_message[i:i + 2]
        decrypted_message += decrypt_pair(square, pair)

    return decrypted_message

if __name__ == "__main__":
   
    full_name = input("Enter your full name: ")

    
    key = "ENCRYPTION"

    
    playfair_square = generate_playfair_square(key)

   
    encrypted_name = encrypt(full_name, playfair_square)
    print(f"Encrypted name: {encrypted_name}")

    
    decrypted_name = decrypt(encrypted_name, playfair_square)
    print(f"Decrypted name: {decrypted_name}")