#try again function
def try_again(again):
    while True:
        answer = input('Do you want to use the DECRYPTOR again? ')
        if answer in ["Y", "YES", "yes", "Yes", "y"]:
            return True
        elif answer in ["N", "NO", "no", "No", "n"]:
            print('Thank you for using the decryptor')
            return False
        else:
            print('Try answering either YES or NO')

#decrypt function
def decryptor():
#asks user input of encrypted text
    e_text = input('Write the encrypted text you want to decrypt: ')
#replaces each character with a specific character
    d_text = e_text.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')
#prints decrypted text
    print(f'The message from the encrypted text: {d_text}')
#returns decrypted text
    return d_text

#sample input: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g

again = True
while again:
    d_text = decryptor()
    again = try_again(again)
