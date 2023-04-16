#try again function
def try_again():
    again = None
    while again is None:
        answer = input('Do you want to use the DECRYPTOR again? ')
        if answer == "Y" or answer == "YES" or answer == "yes" or answer == "Yes" or answer == "y":
            again = str(answer)
            continue
        elif answer == "N" or answer == "NO" or answer == "no" or answer == "No" or answer == "n":
            again = str(answer)
            print('Thank you for using the decryptor')
            break
        else:
            print('Try answering either YES or NO')

#decrypt function
def decryptor():
#replaces each character with a specific character
    d_text = e_text.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')
#returns decrypted text
    return d_text
#asks user input of encrypted text
e_text = input('Write the encrypted text you want to decrypt: ')
#program decrypts the encrypted text
d_text = decryptor(e_text)
#prints decrypted text
print(f'The message from the encrypted text is {d_text}')

#sample input: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g
