s = input("enter the text: ")

max_var = 0
start = 0
char_idx = {}

for i in range(len(s)):
    if s[i] in char_idx and char_idx[s[i]] >= start:
        start = char_idx[s[i]] + 1
    char_idx[s[i]] = i
    max_var = max(max_var, i - start + 1)

print(max_var)