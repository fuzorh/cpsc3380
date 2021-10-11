"""
This is a python file used for decrypting plain text using Vigenere Cipher (Polyalphabetic).
"""

def decrypt():
    
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
            
    # decrypt text uses the key
    
    orig_text = []
    for i in range(len(message)):
        x = (ord(message[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
     

if __name__ == "__main__":
    print(decrypt())