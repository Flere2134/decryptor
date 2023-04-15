#try again function
def try_again():
    again = None
    while again is None:
        answer = input('Do you want to use the DECRYPTOR again? ')
        if answer == "Y" or "YES" or "yes" or "Yes":
            again = str(answer)
            continue
        elif answer == "N" or "NO" or "no" or "No":
            again = str(answer)
            print('Thank you for using the decryptor')
            break
        else:
            print('Try answering either YES or NO')
