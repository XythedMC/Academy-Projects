def perm(text: str) -> list:
    if len(text) < 2:
        return [text]
    res = []
    for i in range(len(text)):
        first = text[i]
        all_perms = perm(text[:i] + text[i + 1:])
        for sub_perm in all_perms:
            res.append(first + sub_perm)

    return sorted(res)

print(perm(input("")))