profile = {
    'name': 'Sohel',
    'age': 29,
    'hobbies': ['Reading books', 'Playing Cards', 'Learn technologies']
}

# profile.pop('name')
# print(profile.get('age'))
# print(profile.keys())
# print(profile.items())
# profile.popitem()
try:
    hobbies = profile['hobbies']

    for hobby in hobbies:
        print(hobby)
    # print(profile['hobbies'])
except:
    print('Key not found!')

