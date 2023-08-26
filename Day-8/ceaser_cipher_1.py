import art

alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function 'encrypt' or 'decrypt' a message that takes text input and shifts it

def ceaser(message, shift_amount, cipher_direction):
    ceaser_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if (new_position > 25):
                new_position = new_position - 26
            new_letter = alphabet[new_position]
            ceaser_text += new_letter
        else:
            ceaser_text += char

    print(f"The encoded text is {ceaser_text}")


print(f"{art.logo}")

while (True):
    direction = input("Type 'encode' to encrypt, type 'decode ' to decrypt:\n")
    if (direction != "encode") and (direction != "decode"):
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(plain_text=text, shift_amount=shift, cipher_direction=direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if go_again == "yes":
        continue
    elif go_again == "no":
        print("Goodbye")
        break
    else:
        print("Wrong choice. Going again")