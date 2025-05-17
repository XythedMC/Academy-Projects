def str_to_int_list(input: str, delimiter: str = ',') -> list[int]:
    return [int(i) for i in input.split(delimiter)]

text = input("please enter number:")
res = str_to_int_list(text)
res_sum = 0
for i in res:
    res_sum += i
print(res, len(res), res_sum)
