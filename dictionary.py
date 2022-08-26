profile = {
    'name': 'Sohel',
    'age': 29,
    'hobbies': ['Reading books', 'Playing Cards', 'Learn technologies']
}

profile.pop('name')

try:
    hobbies = profile['hobbies']

    for hobby in hobbies:
        print(hobby)
    # print(profile['hobbies'])
except:
    print('Key not found!')

