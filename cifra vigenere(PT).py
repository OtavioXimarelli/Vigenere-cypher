def get_user_input(prompt):
    """
    Solicita uma entrada ao usuário e retorna como string.
    """
    return input(prompt)
    
def vigenere(message, key, direction=1):
    """
    Implementa a cifra de Vigenère para criptografar ou descriptografar uma mensagem.
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
    Solicita ao usuário a mensagem e a chave, e criptografa a mensagem usando a cifra de Vigenère.
    """
    text = get_user_input('DIGITE SEU TEXTO PARA CRIPTOGRAFAR: ')
    key = get_user_input('DIGITE SUA CHAVE DE CRIPTOGRAFIA: ')
    encrypted_text = vigenere(text, key)
    print('TEXTO CRIPTOGRAFADO: ', encrypted_text)

def decrypt_message():
    """
    Solicita ao usuário a mensagem criptografada e a chave, e descriptografa a mensagem usando a cifra de Vigenère.
    """
    text = get_user_input('Digite seu texto criptografado: ')
    key = get_user_input('Digite sua chave para descriptografia: ')
    decrypted_text = vigenere(text, key, -1)
    print('TEXTO DESCRIPTOGRAFADO:', decrypted_text)

def main():
    """
    Função principal que solicita ao usuário a ação desejada (criptografar ou descriptografar).
    """
    modo = int(input('O que deseja fazer? Digite 1 para criptografar e 2 para descriptografar: '))
    if modo == 1:
        encrypt_message()  # Correção: Adiciona parênteses para chamar a função
    elif modo == 2:
        decrypt_message()
    else:
        print('Opção inválida. Digite 1 para criptografar e 2 para descriptografar.')
    
if __name__ == "__main__":
    main()
