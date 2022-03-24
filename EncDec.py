#encoding and decoding text with utf-8 in python
import sys

script, input_encoding, error = sys.argv

def main(lang, encoding, errors):
    line = lang.readline()

    #if there exists bytes in the line, encode the contents of the line
    if line:
        print_line(line, encoding, errors)
        return main(lang, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    byte_string = next_lang.encode(encoding, errors = errors)
    utf_string = byte_string.decode(encoding, errors = errors)

    # return each encoded line from the textfile with the equivalent original text 
    print(byte_string, "<====>", utf_string)

languages = open("lang.txt", encoding = "utf-8")

main(languages, input_encoding, error)