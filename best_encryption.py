# best.py
import time
import base64
from cryptography.fernet import Fernet
import rsa


def base64_encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def base64_decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def fernet_encrypt_decrypt(msg):
    key = Fernet.generate_key()
    f = Fernet(key)
    enc = f.encrypt(msg.encode())
    dec = f.decrypt(enc).decode()
    return enc, dec


def rsa_encrypt_decrypt(msg):
    pubkey, privkey = rsa.newkeys(512)
    enc = rsa.encrypt(msg.encode(), pubkey)
    dec = rsa.decrypt(enc, privkey).decode()
    return enc, dec


def indexing_encrypt_decrypt(msg, shift=5):
    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    enc = ''
    dec = ''
    for i in msg:
        idx = charset.find(i)
        enc += charset[(idx + shift) % len(charset)]
    for i in enc:
        idx = charset.find(i)
        dec += charset[(idx - shift) % len(charset)]
    return enc, dec


def compare_algorithms(msg, key):
    print("\n--- Comparing Encryption Algorithms ---")

    # Base64 Custom Cipher
    start = time.time()
    enc_b64 = base64_encode(key, msg)
    dec_b64 = base64_decode(key, enc_b64)
    end = time.time()
    print(f"Base64 Cipher - Time: {end-start:.6f}s | Decrypted: {dec_b64}")

    # Fernet
    start = time.time()
    enc_f, dec_f = fernet_encrypt_decrypt(msg)
    end = time.time()
    print(f"Fernet         - Time: {end-start:.6f}s | Decrypted: {dec_f}")

    # RSA
    start = time.time()
    enc_rsa, dec_rsa = rsa_encrypt_decrypt(msg)
    end = time.time()
    print(f"RSA            - Time: {end-start:.6f}s | Decrypted: {dec_rsa}")

    # Index-based
    start = time.time()
    enc_idx, dec_idx = indexing_encrypt_decrypt(msg)
    end = time.time()
    print(f"Indexing       - Time: {end-start:.6f}s | Decrypted: {dec_idx}")


if __name__ == "__main__":
    message = "EncryptMe123"
    key = "mysecretkey"
    compare_algorithms(message, key)
