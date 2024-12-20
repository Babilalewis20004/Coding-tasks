from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save the key to a file
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Function to encrypt data
def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

if __name__ == "__main__":
    data = input("Enter data to encrypt: ")
    encrypted_data = encrypt_data(data)
    print(f"Encrypted data: {encrypted_data}")
