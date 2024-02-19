
# Python Coding Practice 

"""

lecture 3
18 FEB 2024

"""


# def information(**kwargs):
#     print(type(kwargs))
#     print(kwargs["age"])


# json_d = {
#     "school":"ABC", 
#     "name":"xyz", 
#     "age":3, 
#     "is_present":True
# }

# information(**json_d)



# def both_add_and_info(*args, **kwargs):

#     print(args)
#     print(kwargs)

# both_add_and_info(1, 2, name="ABC", age="3")


# nested functions

# def outside():

#     print("Hi I am outside")

#     def inside():

#         print("Hi I am inside")

#     return inside
    
# value = outside()

# value()



# ----------------------------------------------



# Function Returns


# def func_return():
#     x  = 10
#     y = 20
#     z = 30
#     return x, y, z


# value_x, value_y, _  = func_return()

# print(value_x)
# print(value_y)
# print(_)


# def func_return():
#     x  = 10

#     return

# value = func_return()

# print(value)

# ------------------------------------------------------



# Decorators 

# def make_pretty(_):

#     print("I am before Inner")
#     def inner():
#         print("I got decorated")

#     # func()    
#     inner()
#     return _

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# value = ordinary()    

# value()

# parameterized decorators


# def make_pretty(func, name="ABC"):

#     print(f"I am before Inner with {name}")
#     def inner(age):
#         print(f"I got decorated with {name} and {age}")

#     func()


#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary(age=25) 


# Chained Decorators


# def first_dec(func):

#     print("I am first decorator")
#     func()
#     return func

# def sec_dec(func2):

#     print("I am second decorator")
#     func2()
#     return func2


# @first_dec
# @sec_dec
# def our_method():
#     print("I am our method")


# our_method()






