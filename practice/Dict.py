dict1 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
keys = dict1.keys()
for k in keys:
    print("key :" + k)
values = dict1.values()
for v in values:
    print("value :" + v)
items = dict1.items()
for item in items:
    print(item)
    print(type(item))
for k, v in dict1.items():
    print("key :" + k + ";value: " + v)
