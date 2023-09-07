#ver 1
# def func_1(func):
#     def wrapper():
#         print('Begin')
#         func()
#         print('End')
#     return  wrapper()
# @func_1
# def func_2():
#     print('Processing')
# func_2()

#ver2
def func_1(func):
    def wrapper(*args, **kwargs):
        print('Begin')
        func(*args, **kwargs)
        print('End')
    return  wrapper
@func_1
def func_2(message):
    print(message)
@func_1
def func_3(message1, message2):
    print(message1)
    print(message2)

func_2("hello")
print(".................................")
func_3("hi", "Bye")