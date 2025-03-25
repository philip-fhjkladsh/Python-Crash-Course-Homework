# # 练习7.1：汽车租赁
# print("练习7.1：汽车租赁")
# car = input("What kind of car do you want to rent? ")
# print(f"Let me see if I can find you a {car}.")
#
# # 练习7.2：餐馆订位
# print("练习7.2：餐馆订位")
# number = input("How many people will be dining? ")
# number = int(number)
# if number > 8:
#     print("Sorry, but we don't have any available tables.")
# else:
#     print("We have available tables.")
#
# # 练习7.3：10的整数倍
# print("练习7.3：10的整数倍")
# number = input("Enter a number, and I'll tell you if it's a multiple of 10. ")
# number = int(number)
# if number % 10 == 0:
#     print(f"{number} is a multiple if 10.")
# else:
#     print(f"{number} isn't a multiple of 10.")

# # 练习7.4：比萨配料
# print("练习7.4：比萨配料")
# prompt="\nPlease enter the pizza toppings."
# prompt+="\n(Enter 'quit' when you are finished.) "
#
# while True:
#     topping=input(prompt)
#     if topping=='quit':
#         break
#     else:
#         print(f"Adding {topping} to pizza.")

# # 练习7.5：电影票
# print("练习7.5：电影票")
# prompt="\nPlease enter you age."
# prompt+="\n(Enter 'quit' when you are finished.) "
#
# while True:
#     age=input(prompt)
#     if age=='quit':
#         break
#     else:
#         age = int(age)
#         if age=='quit':
#             break
#         elif age<3:
#             fee="$0"
#         elif age<12:
#             fee="$10"
#         else:
#             fee="$15"
#     print(f"Your admission fee is {fee}.")

# # 练习7.6：三种出路
# print("练习7.6：三种出路")
# #练习7.4中利用break来退出循环
# #利用条件测试来结束循环
#
# prompt="\nPlease enter the pizza toppings."
# prompt+="\n(Enter 'quit' when you are finished.) "
#
# topping=""
# while topping!='quit':
#     topping=input(prompt)
#     if topping!='quit':
#         print(f"Adding {topping} to pizza.")

# #利用变量active来控制循环结束的时机
#
# prompt="\nPlease enter the pizza toppings."
# prompt+="\n(Enter 'quit' when you are finished.) "
#
# active=True
# while active:
#     topping=input(prompt)
#     if topping=='quit':
#         active=False
#     else:
#         print(f"Adding {topping} to pizza.")

# 练习7.7：无限循环
# print("练习7.7：无限循环")
#
# times=0
# while True:
#     times += 1
#     print(f"This is an infinite loop. This is {times}th loop.")
