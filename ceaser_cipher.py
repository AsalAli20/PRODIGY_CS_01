letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key
    for letter in text:
        letter = letter.lower()
        if letter != ' ':
            if letter in letters:
                index = letters.index(letter)
                new_index = (index + key) % num_letters
                result += letters[new_index]
            else:
                result += letter
        else:
            result += ' '
    return result


print()
print('ceaser cipher')
print()

print('please choose e if you want to encrypt the message you will enter, otherwise choose d to decrypt it')
user_input =input('e/d: ').lower()
print()

if user_input =='e':
    print('you choose to encrypt your message')
    print()
    key = int(input('enter the key: '))
    text= input('enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text,user_input,key)
    print(f'ciphertext: {ciphertext}')

elif user_input =='d':
    print('you choose to decrypt your message')
    print()
    key = int(input('enter the key: '))
    text= input('enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text,user_input,key)
    print(f'plaintext: {plaintext}')

