# Function to encrypt the message using Caesar Cipher

def encrypt(text, shift):
    result = ""
    
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Keep punctuation and spaces unchanged
    
    return result

# Function to decrypt the message using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is simply encryption with negative shift

# Get user input for message and shift value
def main():
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid option, please choose 'e' or 'd'.")

# Run the program
if __name__ == "__main__":
    main()

