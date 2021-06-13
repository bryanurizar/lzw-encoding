#!/usr/bin/env python3

text = 'a simple script that compares non-adaptive dictionary encoding against lzw encoding and outputs the character count for both non-adaptive dictionary encoding and lzw encoding'

encoding_dictionary = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12',
                       'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', ' ': '27'}

text_list = text.split(' ')


def basic_encoding(text):
    basic_encoding = ''
    for character in text:
        if character in encoding_dictionary.keys():
            character = encoding_dictionary[character]
            basic_encoding += character
    print('Basic Encoding Uses: ' + str(len(basic_encoding)) + ' characters')
    print('Basic Encoding Text:' + basic_encoding)
    return ''


def LZW_encoding(text):
    encoded_text = []
    last_value_used = int(encoding_dictionary[' '])

    for word in text_list:
        if word in list(encoding_dictionary.keys()):
            encoded_text.append(encoding_dictionary[word])
        else:
            last_value_used += 1
            encoding_dictionary[word] = str(last_value_used)

            encoded_word = ''
            for character in word:
                encoded_word += encoding_dictionary[character]
            encoded_text.append(encoded_word)

    LZW_encoded_text = encoding_dictionary[' '].join(encoded_text)
    print('LZW Encoding Uses: ' + str(len(LZW_encoded_text)) + ' characters')
    print('LZW Encoded Text:' + LZW_encoded_text)
    return ''


print(basic_encoding(text))
print(LZW_encoding(text))
