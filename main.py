def caesarEncrypt(key, plainText):
    ciphertext = ""

    if key.isdigit():
        key = int(key)
    else:
        key = key.lower()
        key = int(alphabet.index(key))


    for l in plainText:
        if l == " ":
            ciphertext += l

        else:
            if l.isupper():
                l = l.lower()
                index = (alphabet.index(l) + key) % 26
                ciphertext += alphabet[index].upper()

            else:
                index = (alphabet.index(l) + key) % 26
                ciphertext += alphabet[index]


    print(plainText)
    print(ciphertext)


def caesarKey(plainText, ciphertext):
    plainText, ciphertext = plainText.lower(), ciphertext.lower()

    key = int(alphabet.index(ciphertext[0]) - alphabet.index(plainText[0]))
    if key < 0: key += 26

    keyL = alphabet[key]
    print(key, keyL)


def substitutionCipher(plainText, ciphertext, newText):
    newCipher = ""

    for l in newText:
        if l == " ":
            newCipher += l
        else:
            if l.isupper():
                try:
                    index = plainText.index(l)
                except:
                    l = l.lower()
                    index = plainText.index(l)

                newCipher += ciphertext[index].upper()

            else:
                index = plainText.index(l)
                newCipher += ciphertext[index]

    return newCipher


def deSubstitutionCipher(plainText, ciphertext, newText):
    newCipher = substitutionCipher(ciphertext, plainText, newText)
    return newCipher


def correctSubstitution(plainText, ciphertext, newText, newCipher):
    correctCipher = substitutionCipher(plainText, ciphertext, newText)
    if newCipher == correctCipher: return True
    else: return False




# Main
alphabet = "abcdefghijklmnopqrstuvwxyz"


# Must be string
key = "3"

plainText  = "CDEHINPRSTY"
ciphertext = "XJLAZEVKHOM"

newText   = "THIS SENTENCE IS ENCYPTED"
newCipher = "OAZH HLEOLEXL ZH LEXMVOLJ"


# Casar Encrypt
caesarEncrypt(key, plainText)


# Casar Key
# caesarKey(plainText, ciphertext)


# Substitution Cipher
# print(substitutionCipher(plainText, ciphertext, newText))


# DeSubstitution Cipher
# print(deSubstitutionCipher(plainText, ciphertext, newText))


# Correct Substitution
# print(correctSubstitution(plainText, ciphertext, newText, newCipher))