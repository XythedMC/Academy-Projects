def isPal(text: str) -> bool:
    if len(text) == 1:
        return True
    if len(text) % 2 == 0:
        return False
    return isPal(text[1:-1]) if text[0] == text[-1] else False

print(isPal(input("")))