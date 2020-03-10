import argparse
import sys


def define_parameters():
    parser = argparse.ArgumentParser()

    parser.add_argument("Cipher_type", default="shift", type=str,
                        help="shift , affine or vigenere")
    parser.add_argument("Operation_type", default="dec", type=str,
                        help="enc or dec")
    parser.add_argument("input", default="input", type=str,
                        help="the input file")
    parser.add_argument("output", default="output", type=str,
                        help="the output file")
    parser.add_argument("encryption_keys", default=[7], type=list,
                        help="Path of the output file")
    return parser.parse_args()
args = define_parameters()
fileIn = open(args.input,'r')
fileOut = open(args.output, 'w')


alphabet = 'abcdefghijklmnopqrstuvwxyz'
def shiftCipherEnc():
    key = int(args.encryption_keys[0])

    enc = ''
    if fileIn.mode == 'r':
        s= fileIn.read()
        for i in s:
            if i == "\n":
                fileOut.write(enc + '\n')
                enc = ''
            i = i.lower()
            pos = alphabet.find(i)
            newPos = (pos+key)%26
            enc += alphabet[newPos]

        print(enc)


def shiftCipherDec():
    key = int(args.encryption_keys[0])

    dec = ''
    if fileIn.mode == 'r':
        s = fileIn.read()
        for i in s:
            if i == "\n":
                fileOut.write(dec + '\n')
                dec = ''
            i = i.lower()
            pos = alphabet.find(i)
            newPos = (pos-key)%26
            dec += alphabet[newPos]

        # fileOut.write(dec + "\n")

def afineCipherEnc():
    a = int(args.encryption_keys[0]) # add the two numbers without space
    b = int(args.encryption_keys[1])
    enc = ''
    if fileIn.mode == 'r':
        s = fileIn.read()
        for i in s:
            if i == "\n":
                fileOut.write(enc + '\n')
                enc = ''
            i = i.lower()
            pos = alphabet.find(i)
            newPos = (a*pos + b) %26
            enc += alphabet[newPos]

        # fileOut.write(enc + "\n")

def afineCipherDec():
    a = args.encryption_keys[0]
    b = args.encryption_keys[1]
    dec = ''
    for i in range(1, 26):
        x = (i * a) % 26
        if x == 1:
            a = i
        else:
            a = -1

    if fileIn.mode == 'r':
        s = fileIn.read()
        for i in s:
            if i == "\n":
                fileOut.write(dec + '\n')
                dec = ''
            i = i.lower()
            pos = alphabet.find(i)
            newPos = (a * pos + b) % 26
            dec += alphabet[newPos]

        # fileOut.write(dec + "\n")

def vigenereCipherEnc():
    if fileIn.mode == 'r':
        plain_text = fileIn.read()
        input_lines=plain_text.split('\n')
        for line in input_lines :
            cipher_text=""
            keyword = args.encryption_keys
            for i in range(len(line) - len(keyword)):
                keyword+=keyword[i]
            for i in range(len(line)):
                if line[i].isupper() and keyword[i].isupper():
                    x = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 65)
                    cipher_text += chr((((x + k) % 26) + 65))
                elif line[i].isupper() and keyword[i].islower():
                    x = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 97)
                    cipher_text += chr((((x + k) % 26) + 65))
                elif line[i].islower() and keyword[i].isupper():
                    x = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 65)
                    cipher_text += chr((((x + k) % 26) + 97))
                elif line[i].islower() and keyword[i].islower():
                    x = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 97)
                    cipher_text += chr((((x + k) % 26) + 97))

            fileOut.write(cipher_text+"\n")

def vigenereCipherDec():
    if fileIn.mode == 'r':
        cipher_text = fileIn.read()
        input_lines = cipher_text.split('\n')
        for line in input_lines:
            plain_text = ""
            keyword = args.encryption_keys
            for i in range(len(line) - len(keyword)):
                keyword += keyword[i]
            for i in range(len(line)):
                if line[i].isupper() and keyword[i].isupper():
                    y = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 65)
                    plain_text += chr((((y - k + 26) % 26) + 65))
                elif line[i].isupper() and keyword[i].islower():
                    y = (ord(line[i]) - 65)
                    k = (ord(keyword[i]) - 97)
                    plain_text += chr((((y - k + 26) % 26) + 65))
                elif line[i].islower() and keyword[i].isupper():
                    y = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 65)
                    plain_text += chr((((y - k + 26) % 26) + 97))
                elif line[i].islower() and keyword[i].islower():
                    y = (ord(line[i]) - 97)
                    k = (ord(keyword[i]) - 97)
                    plain_text += chr((((y - k + 26) % 26) + 97))

            fileOut.write(plain_text+"\n")

if __name__ == "__main__":

    if define_parameters().Cipher_type == "shift":
        if define_parameters().Operation_type == "enc":
            shiftCipherEnc()
        elif define_parameters().Operation_type == "dec":
            shiftCipherDec()

    elif define_parameters().Cipher_type == "affine":
        if define_parameters().Operation_type == "enc":
            afineCipherEnc()
        elif define_parameters().Operation_type == "dec":
            afineCipherDec()

    elif define_parameters().Cipher_type == "vigenere":
        if define_parameters().Operation_type == "enc":
            vigenereCipherEnc()
        elif define_parameters().Operation_type == "dec":
            vigenereCipherDec()
