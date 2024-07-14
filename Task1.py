def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)  # encrypting with negative shift

def main():
    print("Welcome to the Caesar Cipher encryption/decryption tool!")
    
    while True:
        try:
            text = input("\nEnter the message you want to encrypt or decrypt (letters and spaces only): ")
            shift = int(input("Enter the shift value (positive integer): "))
            
            if shift < 1:
                print("Shift value must be a positive integer. Please try again.")
                continue
            
            encrypted_text = caesar_cipher_encrypt(text, shift)
            decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
            
            print("\nEncryption and decryption completed successfully!")
            print(f"Original message: {text}")
            print(f"Encrypted message: {encrypted_text}")
            print(f"Decrypted message: {decrypted_text}")
            
            break 
        
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the shift value.")
        except Exception as e:
            print(f"An error occurred: {str(e)}. Please try again.")

if __name__ == "__main__":
    main()
