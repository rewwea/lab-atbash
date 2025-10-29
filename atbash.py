def atbash_encrypt(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Входные данные должны быть строкой")

    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr(155 - ord(ch)))
        elif 'a' <= ch <= 'z':
            result.append(chr(219 - ord(ch)))
        else:
            result.append(ch)
    return ''.join(result)


def atbash_decrypt(text: str) -> str:
    return atbash_encrypt(text)