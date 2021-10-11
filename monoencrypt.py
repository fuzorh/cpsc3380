"""
This is a python file used for encrypting plain text using St Cyr Cipher (Monoalphabetic).
"""
def encryptMessage():
    
    alphabetUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetLow = "abcdefghijklmnopqrstuvwxyz"

    encrypted = ""

    message = input("Enter the message you want to encrypt: ")
    key = input("Enter your encryption key (1-25): " )

    for m in message:
        if (m.isupper()):
            alphabet = alphabetUp
        else:
            alphabet = alphabetLow
        if m in alphabet:
            location = alphabet.index(m)
            location += int(key)
            if (location > len(alphabet)):
                encrypted += alphabet[(location % 25) - 1]
            else:
                encrypted += alphabet[location]
        else: encrypted += m
    return encrypted
    
if __name__ == "__main__":
    print(encryptMessage())