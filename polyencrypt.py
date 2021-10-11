"""
This is a python file used for encrypting plain text using Vigenere Cipher (Polyalphabetic).
"""

def encrypt():
    
    # Get message and key
    message = input("Enter the message you want to encrypt: ")
    key = input("Enter your encryption key (1-25): " )
 
    # Generates key to match the length of original text

    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) -
                       len(key)):
            key.append(key[i % len(key)])
     
    # encrypt text uses the key
    
    cipher_text = []
    for i in range(len(message)):
        x = (ord(message[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

if __name__ == "__main__":
    print(encrypt())