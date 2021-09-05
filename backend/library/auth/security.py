def encrypt_caesar(key, message):
    alpha = "0123456789"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt_caesar(key, message):
    alpha = "0123456789"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


#Vigenere Cipher

def generate_key_vigenerce_cipher(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encryption_vigenerce_cipher(string, key):
  encrypt_text = []
  for i in range(len(string)):
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A')
    encrypt_text.append(chr(x))
  return("" . join(encrypt_text))

def decryption_vigenerce_cipher(encrypt_text, key):
  orig_text = []
  for i in range(len(encrypt_text)):
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A')
    orig_text.append(chr(x))
  return("" . join(orig_text))



# PLAYFAIR
key = "MONARCHY"
key = key.replace(" ", "")
key = key.upper()


def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


result = list()
for c in key:  # storing key
    if c not in result:
        if c == 'J':
            result.append('I')
        else:
            result.append(c)
flag = 0
for i in range(65, 91):  # storing other character
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))
k = 0
my_matrix = matrix(5, 5, 0)  # initialize matrix
for i in range(0, 5):  # making matrix
    for j in range(0, 5):
        my_matrix[i][j] = result[k]
        k += 1


def locindex(c):  # get location of each character
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc


def encrypt_playfair(message):  # Encryption
    result = ""
    message = message.upper()
    message = message.replace(" ", "")
    i = 0
    for s in range(0, len(message) + 1, 2):
        if s < len(message) - 1:
            if message[s] == message[s + 1]:
                message = message[:s + 1] + 'X' + message[s + 1:]
    if len(message) % 2 != 0:
        message = message[:] + 'X'
    while i < len(message):
        loc = list()
        loc = locindex(message[i])
        loc1 = list()
        loc1 = locindex(message[i + 1])
        if loc[1] == loc1[1]:
            result = result + my_matrix[(loc[0] + 1) % 5][loc[1]]+ my_matrix[(loc1[0] + 1) % 5][loc1[1]] + " "
        elif loc[0] == loc1[0]:
            result = result + my_matrix[loc[0]][(loc[1] + 1) % 5]+ my_matrix[loc1[0]][(loc1[1] + 1) % 5] + " "
        else:
            result = result + my_matrix[loc[0]][loc1[1]]+ my_matrix[loc1[0]][loc[1]] + " "
        i = i + 2

    return result.strip()


def decrypt_playfair(message):  # decryption
    result = ""
    message = message.upper()
    message = message.replace(" ", "")
    i = 0
    while i < len(message):
        loc = list()
        loc = locindex(message[i])
        loc1 = list()
        loc1 = locindex(message[i + 1])
        if loc[1] == loc1[1]:
            result = result + my_matrix[(loc[0] - 1) % 5][loc[1]] + my_matrix[(loc1[0] - 1) % 5][loc1[1]]
        elif loc[0] == loc1[0]:
            result = result + my_matrix[loc[0]][(loc[1] - 1) % 5] + my_matrix[loc1[0]][(loc1[1] - 1) % 5]
        else:
            result = result + my_matrix[loc[0]][loc1[1]] + my_matrix[loc1[0]][loc[1]]

        i = i + 2

    return result.strip()

