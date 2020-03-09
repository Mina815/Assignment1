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

        fileOut.write(dec + "\n")

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

        fileOut.write(enc + "\n")

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

        fileOut.write(dec + "\n")



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

