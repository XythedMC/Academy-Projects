text = input("")

def split_list(text: str):
    if len(text) == 0:
        return None
    res = split_list(text[1:])
    return [text[0]] + res if res is not None else [text[0]]

lst = split_list(text)

def list_to_dict(letters) -> dict:
    res = {}
    for i in range(len(letters)):
        res[letters[i]] = i
    return res

lst = sorted(list(set(lst)))

res = list_to_dict(lst)

print(res)
