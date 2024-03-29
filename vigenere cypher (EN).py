def get_user_input(prompt):
    """
    Requests input from the user and returns it as a string.
    """
    return input(prompt)
    
def vigenere(message, key, direction=1):
    """
    Implements the Vigenère cipher to encrypt or decrypt a message.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]   
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt_message():
    """
    Requests the message and the key from the user, and encrypts the message using the Vigenère cipher.
    """
    text = get_user_input('ENTER YOUR TEXT TO ENCRYPT: ')
    key = get_user_input('ENTER YOUR ENCRYPTION KEY: ')
    encrypted_text = vigenere(text, key)
    print('ENCRYPTED TEXT: ', encrypted_text)

def decrypt_message():
    """
     Requests the encrypted message and the key from the user, and decrypts the message using the Vigenère cipher.
    """
    text = get_user_input('ENTER YOUR TEXT TO DECRYPT: ')
    key = get_user_input('ENTER YOUR DECRYPTION KEY: ')
    decrypted_text = vigenere(text, key, -1)
    print('DECRYPTED TEXT:', decrypted_text)

def main():
    """
     Main function that requests the desired action from the user (encrypt or decrypt).
    """
    mode = int(input('WHAT DO YOU WANT TO DO? TYPE 1 TO ENCRYPT AND 2 TO DECRYPT:  '))
    if mode == 1:
        encrypt_message()
    elif mode == 2:
        decrypt_message()
    else:
        print('INVALID OPTION. TYPE 1 TO ENCRYPT AND 2 TO DECRYPT.')
    
if __name__ == "__main__":
    main()
