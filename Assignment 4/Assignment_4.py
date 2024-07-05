def caesar_encrypt(text, shift):
    """Encrypts the text with caesar cipher."""
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 +
                                  ascii_offset)
        elif char.isdigit():
            ascii_offset = 48
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 10 +
                                  ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    """Decrypts the text with caesar cipher."""
    return caesar_encrypt(text, -shift)


def main():
    """Entry point of the program."""
    mode = input('Choose mode(encrypt/decrypt): ')
    if mode not in ['encrypt', 'decrypt']:
        print('Invalid mode')
        return

    filename = input('Input file path: ')
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f'{filename} not found')
        return

    shift = input('Enter shift key (an integer value): ')
    if not shift:
        print('Shift key cannot be empty')
        return
    try:
        shift = int(shift)
    except ValueError:
        print('Shift key must be an integer')
        return

    if mode == 'encrypt':
        new_text = caesar_encrypt(text, shift)
    else:
        new_text = caesar_decrypt(text, shift)

    new_filename = input('Output file path: ')
    try:
        with open(new_filename, 'w') as file:
            file.write(new_text)
    except IOError:
        print("Error happened while writing to file")
        return

    print(f'The text has been {mode}ed and saved to {new_filename}')


if __name__ == '__main__':
    main()