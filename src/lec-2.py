# Python Coding Practice 

"""

lecture 2
4 FEB 2024

"""


# Dictionary


json_data = {
    "name" : "ABC",
    "new_data" : {
        "name" : "DEF",
        "age" : 20
    },
    "age" : 30,
    "is_present" : True
}

# JSON : JavaScript Object Notation


# print(json_data)
# print(dir(json_data))
# print(type(json_data))


# get all the keys

# print(json_data.keys())

# print(json_data.values())

# print(json_data["age"])

# print(json_data.get("age", 0))

# print(json_data.get("school", None))



# Loops                     
#                 -5 -4 -3 -2 -1
#            0 1 2 3 4 5 6 7 8 9  
numbers = [0,1,2,3,4,5,6,7,8,9]

word = "ABCDEFGHIJKLMNOPQR"


# For Loop

# for number in numbers:
#     print(number)

# for character in word:
#     print(character)


# for i in range(10):
#     print(f"index {i} : {numbers[i]}")

# for number in numbers:
#     print(f"Index {numbers.index(number)} : {number}") 


# for i in range(0,10):
#     print(f"index {i} : {numbers[i]}")

# for i in range(0,10,3):
#     print(f"index {i} : {numbers[i]}")


# for i in range(10):
#     print(f"index {i} : {numbers[i-1]}")


# TODO: For loop for Reverse iteration

# i = 0

# while i < len(numbers):
#     print(f"index {i} : {numbers[i]}")

#     i += 1


# Walrus Operator := or assignment expression operator


# if i:= 0 is 0:
#     print(True)

# Operators Exercise
    
#  == = is
# != = is not
# in
# all
# any


# print(flag := True)

# print(flag)


# print(flag := 0)

# print(flag)


# if flag := 30:

#     print(flag)



# Careful

# while i:= 0 < len(numbers):
#     print(f"index {i} : {numbers[i]}")

#     i += 1



# Slicing

numbers = [0,1,2,3,4,5,6,7,8]

# slice with lower/start and upper/end limit
# print(numbers[1:4])

# # slice with only upper limit
# print(numbers[:5])

# # slice with lower limit 
# print(numbers[6:])
# print(numbers)

# # stepwise slice 
# print(numbers[0:9:3])

# reverse list

# print(numbers[::-1])

# print(numbers[::2])
# print(numbers[::-2])


# List Comprehension

# new_numbers_list  = []
# for number in numbers:
#     if number % 2 == 0:
#         new_numbers_list.append(number)


# print("New List without LC : ", new_numbers_list)
# print("New List with LC : ", [number for number in numbers if number % 2 == 0])


# print([character for character in word if True])


# String Operations

# print("-".join(word))

# name_with_pattern = "abc-def-ghi-jkl"
# address = "bosch, bgsw office, new mico road,adugodi, bengluru"


# print(
#     name_with_pattern.split("-")
# )


# print(address.split(","))


# lambda functions / inline functions / annonymous functions


# def add_two_numbers(number1: int, number2:int) -> int:
#     """
#     """

#     return number1 + number2

# print(add_two_numbers(10,20))


# add = add_two_numbers

# print(add(20,30))


# lambda

# print((lambda number1, number2: number1 + number2 )(40,20))



# add_two_numbers = lambda number1, number2: number1 + number2 


# print(add_two_numbers(10,number2=50))


# multiple arguments and keyword arguments

# def addition(*args):

#     sumation = 0
#     for arg in args:
#         sumation += arg
#     return sumation

# print(addition(10,20,30,40,50))



# def information(**kwargs):

#     print(kwargs)

#     print(f"My school is {kwargs['school']}, name is {kwargs['name']}, and is_present value is {kwargs['is_present']}, roll no is {kwargs['roll_no']}")

# information(school="ABC", name="xyz", age=3, is_present=True, roll_no=40)


######################################################### EOD

