from cryptography.fernet import Fernet

# Generate a key to encrypt
key = Fernet.generate_key()

# Write the key information to a file
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Create a Fernet object for encryption
cipher = Fernet(key)

# Get the message
message = input("Please enter the message to be encrypted: ")

# Encrypt the message
encrypted_message = cipher.encrypt(message.encode())

# Write the encrypted message to a file
with open('encrypted.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_message)
print("Your Message Has Been Encrypted: ", encrypted_message)
