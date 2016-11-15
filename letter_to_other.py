# Created on 15 Nov 2016
# Created by: Matthew Lourenco
# This is a program that lets you input a letter then tells you the unicode number for it and the hexadecimal

def convert_to_hexadecimal(input):
    first_number = input // 4096
    second_number = (input % 4096) // 256
    third_number = ((input % 4096) % 256) // 16
    fourth_number = ((input % 4096) % 256) % 16
    
    if first_number > 9:
        first_number = str(unichr(first_number + 55))
    if second_number > 9:
        second_number = str(unichr(second_number + 55))
    if third_number > 9:
        third_number = str(unichr(third_number + 55))
    if fourth_number > 9:
        fourth_number = str(unichr(fourth_number + 55))
    
    print("The hexadecimal equivalent for the first symbol in " + '"' + str(user_input) + '"' + " is: " + str(first_number) + str(second_number) + str(third_number) + str(fourth_number))

user_input = raw_input('Enter a symbol. (If more than one symbol is entered the first will be used) -> ')
count = 0
while not unichr(count) == user_input[0]:
    count = count + 1
print("The unicode equivalent for the first symbol in " + '"' + str(user_input) + '"' + " is: " + str(count))
convert_to_hexadecimal(count)
