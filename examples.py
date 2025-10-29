from atbash import atbash_encrypt
from atbash_caesar import atbash_caesar

examples = ["Hello, World!", "Python", "Zoo", "123!@#"]

print("Примеры (Atbash):")
for e in examples:
    print(f"{e} -> {atbash_encrypt(e)}")

print("\nПримеры (Atbash + Caesar shift=1):")
for e in examples:
    print(f"{e} -> {atbash_caesar(e, 1)}")