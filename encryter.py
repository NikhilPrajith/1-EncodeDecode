import base64
#Nikhil Prajith Kumar Oct 28 2018

def encode(key, text):
    lett = []
    for i in range(len(text)):
        encodeChar = chr(ord(text[i]) + key)
        lett.append(encodeChar)
        encodeChar = chr(ord(text[i]))
        lett.append(encodeChar + "En")
    return base64.urlsafe_b64encode("".join(lett).encode()).decode()


def decode(key, text):
    encodeText = base64.urlsafe_b64decode(text).decode()
    dec = []
    for i in range(len(encodeText) - 1):
        letterNum = ord(encodeText[i]) - key
        letterNum2 = ord(encodeText[i + 1])
        if ((letterNum > 0 and letterNum < 256) and (letterNum2 > 0 and letterNum2 < 256)):
            if (letterNum == letterNum2):
                dec.append(chr(letterNum))
    return "".join(dec)


def askKey():
    key = input("Enter key(number greater than 0): ")
    if (int(key) == 0):
        print("Error, key=0. Try again!")
        askKey()
    return int(key)


def main():
    choice = input("Would you like to decode or encode? ")
    if (choice.lower() == "encode" or choice.lower() == "e"):
        key = askKey()
        text = input("Enter text to encode: ")
        print(encode(key, text))
    elif (choice.lower() == "decode" or choice.lower() == "d"):
        key = askKey()
        text = input("Enter text to decode: ")
        print(decode(key, text))
    else:
        print("Error input. Try again!")
        main()

    print("")
    tryA = input("To encrypt or decryt again enter 'a': ")
    if (tryA.lower() == "a"):
        main()
    else:
        print("Thank you have a wonderful day!")


main()
