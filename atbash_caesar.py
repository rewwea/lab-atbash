from atbash import atbash_encrypt

def atbash_caesar(text: str, shift: int = 3) -> str:
    if not isinstance(text, str):
        raise TypeError("Входные данные должны быть строкой")

    encrypted = atbash_encrypt(text)
    result = []

    shift %= 26
    for ch in encrypted:
        if 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        elif 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        else:
            result.append(ch)
    return ''.join(result)