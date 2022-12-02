import os
import sys


# ENCRPYTION AND DECRYPTION FUNCTIONS
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


# MENU FUNCTIONS
def mainMenu():
    try:
        if sys.platform.startswith('win32'):
            os.system('cls')
        else:
            os.system('clear')

        print("""=== Caesar Cipher Program by Group 2 AN41 ===
            1 - Encryption
            2 - Decryption
            3 - Brute Force (No key needed)
            4 - Exit Program""")

        choice = int(input("What would you like to do?: "))
        if choice == 1:
            encMenu()
        elif choice == 2:
            decMenu()
        elif choice == 3:
            'BLANK MUNA'
        elif choice == 4:
            quit()
        else:
            print("Invalid Choice...")
    except:
        print('Invalid Input...')

def encMenu():
    print("""\n=== Caesar Cipher: ENCRYPTION ===\n""")
    try:
        txt = input("Please enter the message you want to encrpyt: ")
        s = int(input("Please enter shift key: "))
        print("Plain Text : " + txt)
        print("Shift Key: " + str(s))
        ans = encryption(txt, s);
        print("Ciphertext: " + ans)
    except:
        print("Invalid Input, try again...")

def decMenu():
    print("""\n=== Caesar Cipher: DECRYPTION ===\n""")
    try:
        txt = input("Please enter the message you want to decrypt: ")
        s = int(input("Please enter shift key: "))
        print("Ciphertext : " + txt)
        print("Shift Key: " + str(s))
        ans = decryption(txt, s);
        print("Plain Text: " + ans)
    except:
        print("Invalid Input, try again...")


mainMenu()
try_again = input("\nTry again? y/n: ").lower()

while try_again == 'y':
    mainMenu()
    try_again = input("\nTry again? y/n: ").lower()

