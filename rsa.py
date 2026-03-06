import random
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(min_val=100, max_val=500):
    p = random.randint(min_val, max_val)
    while not is_prime(p):
        p = random.randint(min_val, max_val)
    return p


def mod_inverse(e, phi):
    # Extended Euclidean algorithm
    old_r, r = e, phi
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_s % phi


def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(message: int, public_key) -> int:
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext: int, private_key) -> int:
    d, n = private_key
    return pow(ciphertext, d, n)


if __name__ == "__main__":
    public_key, private_key = generate_keys()
    print(f"Public key:  (e={public_key[0]}, n={public_key[1]})")
    print(f"Private key: (d={private_key[0]}, n={private_key[1]})")

    message = 42
    cipher = encrypt(message, public_key)
    decoded = decrypt(cipher, private_key)

    print(f"\nOriginal:  {message}")
    print(f"Encrypted: {cipher}")
    print(f"Decrypted: {decoded}")
