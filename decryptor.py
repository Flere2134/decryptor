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

try_again()
