# practice 6.1
print("练习6.1")
information = {'first_name': 'william', 'last_name': 'shakespeare', 'age': '18', 'city': 'london'}
print(information)

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

#practice 6.4
print("\n练习6.4")
vocabularies = {'del': '删除', 'code': '编程', 'book': '书', 'function': '函数', 'method': '方法','print':'打印，输出','syntax':'语法','error':'错误','invalid':'无效','character':'字符'}
for vocabulary,explanation in vocabularies.items():
    print(f"{vocabulary}:{explanation}")

#practice 6.5
print("\n练习6.5")
rivers={'nile':'egypt',
        'amazon':'brazil',
        'yangtze river':'china',
        }
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())
    
#practice 6.6
print("\n练习6.6")
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }
should_be_investigated=['jen','phil','philip','tom']
for name in should_be_investigated:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for participating in the poll.")
    else:
        print(f"{name.title()}, please take our poll!")
