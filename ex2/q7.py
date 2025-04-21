text = input("enter the text: ")

for i in text:
    if not i.isalpha():
        text = text.replace(i, "")
    if i == " ":
        text = "".join(text.split())
text = text.lower()

max = 0
max_letter = ""
count = [None] * 26
for i in text:
    if text.count(i) > max:
        max = text.count(i)
        max_letter = i

print(max_letter)