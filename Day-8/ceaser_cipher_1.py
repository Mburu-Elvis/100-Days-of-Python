alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function 'encrypt' that takes text input and shifts it

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if (new_position > 25):
            new_position = new_position - 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if (new_position < 0):
            new_position = new_position + 26
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

while (True):
    direction = input("Type 'encode' to encrypt, type 'decode ' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift_amount=shift)
    elif direction == "decode":
        decrypt(text, shift_amount=shift)
    else:
        print("please input a valid direction")
    done = input("Enter 'quit' to stop or 'OK' to continue:\n")
    if done == "quit":
        break
    elif done == "OK":
        continue