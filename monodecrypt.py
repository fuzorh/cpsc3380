"""
This is a python file used for decrypting St Cyr Ciphered text (Monoalphabetic).
"""
def decryptMessage():
    
    alphabetUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetLow = "abcdefghijklmnopqrstuvwxyz"
    alphabet = ""

    decrypted = ""

    message = input("Enter the message you want to decrypt: ")
    key = input("Enter your decryption key 1-25: ")
    
    for e in message:
        if (e.isupper()):
            alphabet = alphabetUp
        else:
            alphabet = alphabetLow
        if e in alphabet:
            location = alphabet.index(e)
            location -= int(key)
            if (location < 0):
                print(location)
                location += len(alphabet)
                print(location)
                decrypted += alphabet[location ]
            else:
                decrypted += alphabet[location]
        else: decrypted += e
    return decrypted
    
if __name__ == "__main__":
    print(decryptMessage())