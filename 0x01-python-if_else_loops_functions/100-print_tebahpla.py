#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_code)
    if (char_code - ord('z')) % 2 == 0:
        print(char.lower(), end='')
    else:
        print(char.upper(), end='')
