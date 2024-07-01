import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

# Check if there are enough command-line arguments
if len(sys.argv) < 3:
    print("Usage: python decrypt.py ENCRYPTED_EMAIL YOUR_SHARED_SECRET_KEY")
    sys.exit(1)

# Hex decode the encrypted email and shared secret key
encryptedEmail = unhexlify(sys.argv[1])
sharedSecretKey = unhexlify(sys.argv[2])

# Initialize Crypt_AES class
cipher = AES.new(sharedSecretKey, AES.MODE_ECB)

# Perform decryption and unpad the result
decrypted = unpad(cipher.decrypt(encryptedEmail), AES.block_size)

print("Decrypted Email:", decrypted.decode('utf-8'))