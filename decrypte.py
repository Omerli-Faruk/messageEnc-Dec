from cryptography.fernet import Fernet

# Şifrelenmiş mesajı okuyun
with open('encrypted.txt', 'rb') as file:
    encrypted_message = file.read()

# Anahtar dosyasını okuyun
with open('key.key', 'rb') as file:
    key = file.read()

# Fernet nesnesi oluşturun
fernet = Fernet(key)

# Şifreyi çözün
decrypted_message = fernet.decrypt(encrypted_message)

# Şifresi çözülmüş mesajı ekrana yazdırın
print("Mesajın Şifresi Çözüldü: ", decrypted_message.decode())
