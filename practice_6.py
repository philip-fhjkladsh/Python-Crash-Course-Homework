# practice 6.1
print("练习6.1")
user_0 = {'first_name': 'william', 'last_name': 'shakespeare', 'age': '52', 'city': 'Warks'}
print(user_0)

# practice 6.2
print("\n练习6.2")
numbers = {
    'jack': 3,
    'philip': 8,
    'phil': 9,
    'tom': 6,
}
print(f"Jack's favorite number is {numbers['jack']}.")
print(f"Philip's favorite number is {numbers['philip']}.")
print(f"Phil's favorite number is {numbers['phil']}.")
print(f"Tom's favorite number is {numbers['tom']}.")

# practice 6.3
print("\n练习6.3")
vocabularies = {'del': '删除', 'code': '编程', 'book': '书', 'function': '函数', 'method': '方法'}
print(f"del:{vocabularies['del']}")
print(f"code:{vocabularies['code']}")
print(f"book:{vocabularies['book']}")
print(f"function:{vocabularies['function']}")
print(f"method:{vocabularies['method']}")

# practice 6.4
print("\n练习6.4")
vocabularies = {'del': '删除', 'code': '编程', 'book': '书', 'function': '函数', 'method': '方法', 'print': '打印，输出',
                'syntax': '语法', 'error': '错误', 'invalid': '无效', 'character': '字符'}
for vocabulary, explanation in vocabularies.items():
    print(f"{vocabulary}:{explanation}")

# practice 6.5
print("\n练习6.5")
rivers = {'nile': 'egypt',
          'amazon': 'brazil',
          'yangtze river': 'china',
          }
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# practice 6.6
print("\n练习6.6")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
should_be_investigated = ['jen', 'phil', 'philip', 'tom']
for name in should_be_investigated:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for participating in the poll.")
    else:
        print(f"{name.title()}, please take our poll!")

# practice 6.7
print("\n练习6.7")
user_0 = {'first_name': 'william', 'last_name': 'shakespeare', 'age': '52', 'city': 'Warks'}
user_1 = {'first_name': 'james', 'last_name': 'joyce', 'age': '59', 'city': 'Paris'}
user_2 = {'first_name': 'david', 'last_name': 'bowie', 'age': '69', 'city': ''}
people = [user_0, user_1, user_2]
for people_number in people:
    print(people_number)

# practice 6.8
print("\n练习6.8")
pet_0 = {'types': 'dog', "owner's name": 'philip'}
pet_1 = {'types': 'fish', "owner's name": 'luke'}
pet_2 = {'types': 'cat', "owner's name": 'phil'}
pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(pet)

# practice 6.9
print("\n练习6.9")
favorite_places = {
    'jack': ['london', 'paris', 'rio'],
    'phil': ['hawaii'],
    'joyce': ['beijing', 'venice'],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(place.title())

# practice 6.10
print("\n练习6.10")
numbers = {
    'jack': [3, 7, 4],
    'philip': [8, 5, 7, 4, 2],
    'phil': [9, 7, 5, 3, 28],
    'tom': [6, 4, 8, 3],
}
for name, favorite_numbers in numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in favorite_numbers:
        print(number)

# practice 6.11
print("\n练习6.11")
cities = {
    'london': {
        'country': "England",
        'population': '8.87 M',
        'fact': "One of the largest cities.",
    },
    'beijing': {
        'country': "China",
        'population': '21.89 M',
        'fact': "The capital of China.",
    },
    'hawaii': {
        'country': "USA",
        'population': '1.44 M',
        'fact': "A very beautiful city.",
    },
}
for name, info in cities.items():
    print(f"\n{name.title()} is belong to {info['country']}, has {info['population']} people.\n{info['fact']}")

# practice 6.11
print("\n练习6.11")
# 调整6.4.3中的示例。添加一对键值，并修改程序。
user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    'jjoyce': {
        'first': 'james',
        'last': 'joyce',
        'location': 'paris'
    }
}
for username, user_info in user.items():
    print(f"\nUsername: {username}"
          f"\n\tFull name: {user_info['first'].title()} {user_info['last'].title()}"
          f"\n\tLocation: {user_info['location'].title()}")
