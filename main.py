def encryption(text, key):
    result = ''
    for i in range(len(text)):
        special = text[i]
        new_special = special.lower()
        if new_special == " ":
            result += ' '
        elif special.isalpha():
            result += chr((ord(new_special) + key - 97) % 26 + 97)

    return result.upper()


def decryption(text, key):
    result = ''
    for i in range(len(text)):
        special = text[i]
        new_special = special.lower()
        if new_special == " ":
            result += ' '
        elif special.isalpha():
            result += chr((ord(new_special) - key - 97) % 26 + 97)
    return result.upper()


# check the above function
def mainMenu():
    print()
    print(""""=== Caesar Cipher Program by Group 2 AN41 ===
        1 - Encryption
        2 - Decryption
        3 - Brute Force (No key needed)
        4 - Exit Program""")

    choice = int(input("What would you like to do? "))
    if choice == 1:
        encMenu()
    elif choice == 2:
        decMenu()
    elif choice == 3:
        'BLANK MUNA'
    elif choice == 4:
        quit()
    else:
        "Invalid Choice, try again"

def encMenu():
    txt = input("Please enter the message you want to encrpyt: ")
    s = int(input("Please enter shift key (0-25): "))
    print("Plain Text : " + txt)
    print("Shift Key: " + str(s))
    ans = encryption(txt, s);
    print("Ciphertext: " + ans)

def decMenu():
    txt = input("Please enter the message you want to decrypt: ")
    s = int(input("Please enter shift key (0-25): "))
    print("Ciphertext : " + txt)
    print("Shift Key: " + str(s))
    ans = encryption(txt, s);
    print("Plain Text: " + ans)

# txt = "CEASER CIPHER EXAMPLE"
# s = 4
#
# print("Plain txt : " + txt)
# print("Shift Key: " + str(s))
# ans = encryption(txt, s);
# print("Cipher: " + ans)
# print("Decrypt: " + decryption(ans, s))

mainMenu()
try_again = input("\nTry again? y/n: ").lower()

while try_again == 'y':
    mainMenu()
    try_again = input("\nTry again? y/n: ").lower()