list = ["a", "b", "c", "d", "e"]

list.remove("b")
stri = ""

# for i in list:
#     stri += str(i) 
#     print(i)

# print('\u0336'.join(str) + '\u0336')

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

text = "HAVEN"
print(strike(text))