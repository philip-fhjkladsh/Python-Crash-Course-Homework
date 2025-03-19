# 练习7.1：汽车租赁
print("练习7.1：汽车租赁")
car = input("What kind of car do you want to rent? ")
print(f"Let me see if I can find you a {car}.")

# 练习7.2：餐馆订位
print("练习7.2：餐馆订位")
number = input("How many people will be dining? ")
number = int(number)
if number > 8:
    print("Sorry, but we don't have any available tables.")
else:
    print("We have available tables.")

# 练习7.3：10的整数倍
print("练习7.3：10的整数倍")
number = input("Enter a number, and I'll tell you if it's a multiple of 10. ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple if 10.")
else:
    print(f"{number} isn't a multiple of 10.")
