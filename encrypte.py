from cryptography.fernet import Fernet

# Şifrelemek için bir anahtar oluşturun
key = Fernet.generate_key()

# Anahtar bilgisini bir dosyaya yazın
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Şifreleme için bir Fernet nesnesi oluşturun
cipher = Fernet(key)

# Mesajı alın
message = input("Lütfen şifrelenecek mesajı girin: ")

# Mesajı şifreleyin
encrypted_message = cipher.encrypt(message.encode())

# Şifreli mesajı bir dosyaya yazın
with open('encrypted.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_message)
print("Mesajınız Şifrelendi: ", encrypted_message)
