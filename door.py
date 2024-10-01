import shutil
columns, rows = shutil.get_terminal_size()

border = "—"

print("Welcome to the DOOR translator!\n\n" + border * columns + "\n")
x = ""

def utf8_to_binary(input_string):
    byte_array = input_string.encode('utf-8')
    binary_string = ''.join(format(byte, '08b') for byte in byte_array)
    return binary_string

def binary_to_door(input_string):
    newstring = ""
    counter = 0
    for c in input_string:
        newchar = ''
        if(counter == 0):
            newchar = 'd'
        if(counter == 1):
            newchar = 'o'
        if(counter == 2):
            newchar = 'o'
        if(counter == 3):
            newchar = 'r'
        if c == '1':
            newchar = newchar.capitalize()
        newstring = newstring + newchar
        if counter == 3:
            newstring = newstring + " "
        counter += 1
        if counter == 4:
            counter = 0
    return newstring

def door_to_binary(input_string):
    newstring = ""
    for c in input_string:
        if c != ' ':
            if c.capitalize() != c:
                newstring = newstring + "0"
            else:
                newstring = newstring + "1"
    return newstring

def binary_to_utf8(input_string):
    integer_value = int(input_string, 2)
    return integer_value.to_bytes((integer_value.bit_length() + 7) // 8, byteorder='big')
while x != "q" and x != "Quit":
    if x == "e" or x == "Encode":
        print("\nResult: " + binary_to_door(utf8_to_binary(input("\nText to encode:\n\t "))) + "\n\n" + border * columns + "\n")
    elif x == "d" or x == "Decode":
        print("\nResult: " + binary_to_utf8(door_to_binary(input("\nText to decode:\n\t "))).decode('utf-8') + "\n\n" + border * columns + "\n")
    else:
        print("To choose what you want to do, type in either 'e', 'd', or 'q'.\ne - Encodes your text into the DOOR language\nd - Decodes your text from DOOR to English\nq - Stops the DOOR translator\n")
    x = input("Encode [e], Decode [d], or Quit [q]? \n\t")
