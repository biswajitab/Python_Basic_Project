# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#     rajesh()
#
# def rajesh():
#     print("lets starr")
# # Calling the decorated function
# say_hello()


# ########Decorator is used to modify the function it take the function as argument
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator       ############decorator
# def say_hello():     ##########this is the function
#     print("Hello!")
#     rajesh()  # Call rajesh inside say_hello
#
# def rajesh():
#     print("lets start")
#
# # Calling the decorated function
# say_hello()
# rajesh()



def my_decorator(func, prin):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        prin()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

def rajesh():
    print("lets start")

# Applying the decorator manually with two functions
decorated_function = my_decorator(say_hello, rajesh)
decorated_function()
