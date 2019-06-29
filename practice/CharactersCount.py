import pprint
message = 'Hello, python; I am studing python language, I studied python two weeks all ready !'
dict2 = {}
for str1 in message:
    dict2.setdefault(str1, 0)
    dict2[str1] = dict2[str1] + 1
for k, v in dict2.items():
    print(k + ":" + str(v) + '\n')
print(dict2)
pprint.pprint(dict2)