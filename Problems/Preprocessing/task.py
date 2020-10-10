text = input()
a = text.lower()
b = a.replace(",", "")
c = b.replace(".", "")
d = c.replace("!", "")
e = d.replace("?", "")

print(e)
