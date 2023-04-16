#try again function
def try_again():
    again = None
    while again is None:
        answer = input('Do you want to use the DECRYPTOR again? ')
        if answer in ["Y", "YES", "yes", "Yes", "y"]:
            again = True
            continue
        elif answer in ["N", "NO", "no", "No", "n"]:
            again = False
            print('Thank you for using the decryptor')
            break
        else:
            print('Try answering either YES or NO')

#decrypt function
def decryptor(e_text):
#replaces each character with a specific character
    d_text = e_text.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')
#asks user input of encrypted text
    e_text = input('Write the encrypted text you want to decrypt: ')
#program decrypts the encrypted text
    d_text = decryptor()
#prints decrypted text
    print(f'The message from the encrypted text: {d_text}')
#returns decrypted text
    return d_text

#sample input: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g

while True:
    decryptor()
    try_again()
    if not again:
        break
