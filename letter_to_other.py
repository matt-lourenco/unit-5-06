# Created on 15 Nov 2016
# Created by: Matthew Lourenco
# This is a program that lets you input a letter then tells you the unicode number for it and the hexadecimal

def convert_to_hexadecimal(input):
    hexadecimal = {'A':'41', 'B':'42', 'C':'43', 'D':'44', 'E':'45', 'F':'46', 'G':'47', 'H':'48', 'I':'49', 'J':'4A', 'K':'4B', 'L':'4C', 'M':'4D', 'N':'4E', 'O':'4F', 'P':'50', 'Q':'51', 'R':'52', 'S':'53', 'T':'54', 'U':'55', 'V':'56', 'W':'57', 'X':'58', 'Y':'59', 'Z':'5A', 'a':'61', 'b':'62', 'c':'63', 'd':'64', 'e':'65', 'f':'66', 'g':'67', 'h':'68', 'i':'69', 'j':'6A', 'k':'6B', 'l':'6C', 'm':'6D', 'n':'6E', 'o':'6F', 'p':'70', 'q':'71', 'r':'72', 's':'73', 't':'74', 'u':'75', 'v':'76', 'w':'77', 'x':'78', 'y':'79', 'z':'7A'}
    
    return hexadecimal[input]

user_input = raw_input('Enter a string of any character. -> ')
for letter in user_input:
    hexadecimal_number = convert_to_hexadecimal(letter)
    print(str(letter) + ' in hexadecimal is -> ' + str(hexadecimal_number))
