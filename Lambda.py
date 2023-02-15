# def multiply(x: int,y: int) -> int:
#     return x * y

# print(multiply(2,3))


# multiplication =  lambda  x,y :  x * y
# print(multiplication(2,3))


# multiplication =  lambda: "Hello World"
# print(multiplication())


# from typing import Callable

# def get_sum(number1: int, number2: int) -> int:
#     return number1 + number2

# def get_something_else() -> str:
#     return "something else"

# def get_function(number:int) -> Callable:
#     if number > 1:
#         return get_sum
#     else:
#         return get_something_else
    
# # my_function = get_function(1)
# # print(my_function())

# print(get_function(2)(1, 2))

# suma = get_sum

# print(suma(5, 5))

from typing import Callable

def my_func(n):
    # return lambda a: a * n
    return lambda a, b, c: (a + b + c) * n

my_doubler = my_func(10)

print(my_doubler(10, 5, 3))