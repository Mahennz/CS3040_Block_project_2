import secrets
import base64

KEY_FILE = None
current_key = None
current_passwords = []

def main():
    print("\n|||||||||||||||||||||||||||\nHello, welcome to Simple_Encryptor!")
    print("This program encrypts passwords using a randomly generated key that you will save.")
    print("Now, do you wish to GEN a new key, INPUTK your key, ENCRYPT a password using a key, DECRYPT a password, or SAVE the encryupted passwords in a text file?.")
    print("\nPlease format your input as: \n No Parameters: \n  SAVE")
    print("\nPlease format your input as: \n Parameters: \n  GEN requires a file path, INPUTK requires a Key.bin file path \n  ENCRYPT followed by a password(only usable if you have inputed or generated a key) \n  DECRYPT followed by a password(only usable if you have inputed or generated a key)")
    
    while True:
        guide_input = input("\nEnter command (GEN, INPUTK, ENCRYPT, DECRYPT, SAVE, QUIT): ").strip()
        
        if not guide_input:
            continue  #ignore empty input

        parts = guide_input.split(maxsplit=1)
        command = parts[0].upper()
        arg = parts[1] if len(parts) > 1 else None

        if command == "GEN":
            path = arg if arg else "key.bin"  #default if no arg given
            generate_key(path)
            print(f"Key generated and saved to {path}")
            KEY_FILE = path
            current_key = load_key(KEY_FILE)

        elif command == "INPUTK":
            if arg is None:
                print("You must provide a path to the key file.")
            else:
                try:
                    current_key = load_key(arg)
                    KEY_FILE = arg
                    print(f"Key loaded from {arg}")
                except FileNotFoundError:
                    print(f"No key found at {arg}")

        elif command == "ENCRYPT":
            if current_key is None:
                print("No key loaded! Generate or input a key first.")
            elif arg is None:
                print("Provide a password to encrypt.")
            else:
                print(f"Encrypted: {encrypt_password(arg, current_key)}")

        elif command == "DECRYPT":
            if current_key is None:
                print("No key loaded! Generate or input a key first.")
            elif arg is None:
                print("Provide text to decrypt.")
            else:
                print(f"Decrypted: {decrypt_password(arg, current_key)}")

        elif command == "SAVE":
            if current_key is None:
                print("No key loaded! Generate or input a key first.")
            else:
                print("Saving passwords to file...")
                save_passwords(current_passwords)

        elif command in ("QUIT", "EXIT"):
            print("Goodbye!")
            break

        else:
            print("Unknown command.")


def generate_key(path, length=32):
    key = secrets.token_bytes(length)
    with open(path, "wb") as f:
        f.write(key)


def load_key(path):
    with open(path, "rb") as f:
        return f.read()


def xor_cipher(data: bytes, key: bytes) -> bytes:
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))


def encrypt_password(password: str, key: bytes) -> str:
    encrypted_bytes = xor_cipher(password.encode(), key)
    current_passwords.append(base64.b64encode(encrypted_bytes).decode())
    return base64.b64encode(encrypted_bytes).decode()


def decrypt_password(ciphertext: str, key: bytes) -> str:
    encrypted_bytes = base64.b64decode(ciphertext)
    decrypted_bytes = xor_cipher(encrypted_bytes, key)
    return decrypted_bytes.decode()


def save_passwords(passwords):
    with open("passwords.enc", "w") as f:
        for p in passwords:
            f.write(p + "\n")





#main call
if __name__ == "__main__":
    main()