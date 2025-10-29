import unittest
from atbash import atbash_encrypt, atbash_decrypt
from atbash_caesar import atbash_caesar

class TestAtbash(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(atbash_encrypt("Hello, World!"), "Svool, Dliow!")
        self.assertEqual(atbash_encrypt("Python"), "Kbgslm")

    def test_symmetry(self):
        text = "Atbash Cipher Test!"
        self.assertEqual(atbash_decrypt(atbash_encrypt(text)), text)

    def test_caesar(self):
        self.assertEqual(atbash_caesar("Hello", 1), "Twppu")

if __name__ == "__main__":
    unittest.main()