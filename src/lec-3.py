
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

# both_add_and_info(1,2,3,4, name="ABC", age="3")


# nested functions

# def outside():

#     print("Hi I am outside")

#     def inside():

#         print("Hi I am inside")

    # inside()
    
# outside()



# ----------------------------------------------



# Function Returns


# def func_return():
#     x  = 10
#     return x



# ------------------------------------------------------



# Decorators 

# def make_pretty(func):

#     print("I am before Inner")
#     def inner():
#         print("I got decorated")

#     func()    


#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()    



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


# def sec_dec(func2):

#     print("I am second decorator")
#     func2()
#     return func2


# @first_dec
# @sec_dec
# def our_method():
#     print("I am our method")






