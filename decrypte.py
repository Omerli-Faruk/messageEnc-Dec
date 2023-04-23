from cryptography.fernet import Fernet

# Read the encrypted message
with open('encrypted.txt', 'rb') as file:
    encrypted_message = file.read()

# Read key file
with open('key.key', 'rb') as file:
    key = file.read()

# Create a Fernet object
fernet = Fernet(key)

# Decrypt the password
decrypted_message = fernet.decrypt(encrypted_message)

# Print the decrypted message to the screen
print("Message Decrypted: ", decrypted_message.decode())
