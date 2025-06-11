a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }

keys = sorted(list(a_dictionary))
print(keys)

for key in keys:
    print(key,":", a_dictionary[key])