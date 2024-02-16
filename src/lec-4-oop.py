# Python Coding Practice 

"""

lecture 2
4 FEB 2024

python -i filename

"""



# Classes


# class Test:

#     def __init__(self):
#         """
#         Constructor
#         """

#         print("I am constructor")


#     def set_name(self, name):
#         """
#         instance method
#         """   

#         self.name = name

    
#     def set_age(self, age):
#         """
#         """

#         self.age = age





# t = Test()

# print(t)

# t.set_name(name="ABC")
# t.set_age(age=3)

# print(t.name)

# print(t.age)


# ================================================


# class Test:
#     """
#     """

#     name_c_a = "ABC"


#     # dunder methods

#     def __init__(self):

#         self.name_i_a = "XYZ"


#     def __name__(self):

#         return "Test Class"


#     def __str__(self):

#         return "I am string "
    

#     def __repr__(self):

#         return f"I am string representation {self.__str__()}"



#     # instance methods
#     def get_name_i_a(self):

#         return self.name_i_a
    
#     def get_name_c_a(self):

#         return self.get_name_c_a


#     # Class Methods
#     @classmethod
#     def get_name_c_a_c_m(cls):

#         return cls.name_c_a
    



# t_obj = Test()

# print(str(t_obj))
# print(t_obj.__repr__())



# Accessing Attributes / Members

# print(t_obj.name_c_a)
# print(t_obj.name_i_a)

# print(Test().name_c_a)
# print(Test().name_i_a)

# print(Test.name_c_a)
# print(Test.name_i_a) # careful


# Accessing Methods

# print(t_obj.__name__())

# print(Test.get_name_c_a_c_m())

# print(Test().get_name_c_a()) # TBChecked
# print(t_obj.get_name_c_a())

# print(Test().get_name_i_a()) 
# print(t_obj.get_name_i_a())



# Public and Private


# class Student:

#     __private_password = "ABCDEFG"
#     public_name = "ABC"
#     def __init__(self):
#         pass

#     def __private_password_method(self):
#         print("I am private Password Method", self.__private_password)


#     def public_name_method(self):
#         print(f"I am public name method {self.public_name}")


    

# s = Student()

# print(s.public_name)
# s.public_name_method()

# print(s.__private_password)
# s.__private_password_method()

# still we can access private members

# print(s._Student__private_password)
# (s._Student__private_password_method)()


# Before Protected we will learn inheritance

# possible inheritance


# simple/single 
# class A:

#     pass

# class B(A):

#     pass



# Hierarchical 

# class A:

#     pass

# class B(A):

#     pass

# class C(A):

#     pass


# multilevel

# class A:

#     pass

# class B(A):

#     pass

# class C(B):

#     pass

# multiple illeagal in java


# class A:

#     pass

# class B:

#     pass

# class C(A, B):

#     pass


# Hybrid


# class A:

#     pass

# class B(A):

#     pass

# class C:

#     pass

# class D(B, C):
#     pass



# Multipath


# class A:

#     pass

# class B(A):

#     pass

# class C(A):

#     pass

# class D(B, C):
#     pass




# Protected and Override method
# class Parent:

#     _name = "I am parent"

#     def __init__(self):
#         pass

#     def _car(self):
#         return "I have Mercedez"

#     def address(self):
#         return "my address is ADDRESS"

# class Child(Parent):

#     _name = "I am child"

#     def __init__(self):
#         pass

#     def address(self):
#         return "my address is NEW ADDRESS"
    
#     def parent_name(self):
#         return "my parent name is " + super()._name


# c = Child()

# print(c.address())
# print(c._name)
# print(c._car())

# # Method Overriding

# print(c.parent_name())



# ====================================

# magic_methods, dunder_methods


class Test:
    """
    __new__ dunder method introductions
    """

    # name = "ABC"
    
    # def __new__(cls):
    #     """
    #     This method is used to create new instance of a class
    #     This method is unique and it's called before __init__()
    #     It returns new instance of class
    #     Used in immutable types and used in metaprogramming
    #     """

    #     print(f"{cls.name} saying Hi from __new__")

    #     # creating parent class's instance
    #     # print(super(Test, cls))

    #     # return super(Test, cls)

    def __init__(self):
        """
        Constructor 
        """

        self.name = "ABC"

        print("saying HI from __init__")


# t_new = Test()
# print(t_new)
# print(dir(t_new))
# print(t_new.name)


class Test:
    """
    Aithmatic and Bitwise Magic Methods
    __eq__ __ne__, 
    __lt__, __le__, __gt__, __ge__
    
    __add__, __sub__, __mul__, __truediv__[/], __floordiv__[//], 
    __mod__, __pow__, __and__[bitwise_and], __invert__[bitwise inversion],
    __or__, __xor__
    """
    def __init__(self, name, age):
        """
        """
        self.name = name
        self.age = age


    def __eq__(self, another_instance):
        """
        asserts attributs and it's values
        """
        return self.name == another_instance.name and self.age == another_instance.age


    def __ne__(self, another_instance):
        """
        asserts attributs and it's values
        """
        return self.name != another_instance.name and self.age != another_instance.age



# t = Test("ABC", 23)

# t1 = Test("XYZ", 30)

# t2 = Test("ABC", 23)

# print(t.__eq__(t1))
# print(t.__eq__(t2))

# print(t.__ne__(t1))
# print(t.__ne__(t2))


class Test:
    """
    Numeric Conversion Magic method
    
    __int__, __float__, __complex__, __str__
    """

    def __init__(self, number, name):
        """
        """

        self.number = number
        self.name = name
        


    def __int__(self):
        """
        """
        self.number = int(self.number)

    
# t = Test(10.3, "float number")

# print(t.number)

# t.__int__()

# print(t.number)


class Test():
    
    """
    Attribute Access and Descriptor
    __getattribute__, __setattr__, __delattr__, __dict__
    """

    def __init__(self, number, name):
        """
        """
        self.number = number
        self.name = name


# t = Test(10, "ABC")

# print(t.name)
# print(t.number)

# print(t.__getattribute__("number"))
# print(t.__getattribute__("name"))

# __getattr__ vs __getattribute__


# t.name = "XYZ"
# t.number = 20

# print(t.name)
# print(t.number)

# t.__setattr__("name", "DEF")
# t.__setattr__("number", 222)

# print(t.name)
# print(t.number)

# print(dir(t))
# print(t.name)

# t.__delattr__("name")

# print(dir(t))

# print(t.name)

# delete attribute with del

# t1 = Test(50, "OIP")
# print(dir(t1))
# print(t1.number)
# del(t1.number)
# print(dir(t1))
# print(t1.number)



# print(t.__dict__)


# =============================== Callable Objects
class Test:
    
    """
    callable objects
    __call__ : allow an instance to be called as a method
    """

    def __init__(self, number, name):
        """
        """
        self.number = number
        self.name = name

    def __call__(self, age):
        self.number += age

# t = Test(20, "ABC")

# print(t.number)

# t(10)

# print(t.number)
        

# -================================ Slots
        
class Test:
    """
    __slots__ : to keep fixed set of attributes
    """

    # __slots__ = ['name', 'age']

    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        

    def add_new_attribute(self):

        self.new_att = "I am new"

# t = Test("ABC", 20)

# print(t.name)
# print(t.age)

# # t.add_new_attribute()

# print(dir(t))
# print(t.__dict__)


# ========================================== Class method and Static Method

class Test:
    """
    class method
    """

    number = 50

    def __init__(self, name, age):

        self.name = name
        self.age = age
        
    @classmethod
    def i_am_class_method(cls):
        # return f"{cls.name} {cls.age}"
        return cls.number
    
    @classmethod
    def object_less_class_method(cls):

        return "I am Object less class method"


# t = Test("ABC", 30)



# print(Test.i_am_class_method()) # careful
# print(t.i_am_class_method())
    
# print(Test.i_am_class_method())

# print(Test.object_less_class_method())
    


class Test:
    """
    static method
    """

    number = 50

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @staticmethod
    def i_am_static():

        return f"I am static method"
    

# t = Test("ABC", 20)

# print(Test.i_am_static())

# print(dir(t))
    

# ================================================== property, getter, setter, deleter
    
class Test:
    """
    property 
    getter
    setter
    deleter
    """

    number = 50

    def __init__(self, name, age):

        self.name = name
        self.age = age
        self._address = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):

        self._address = f"{self.name} --- {address}"    
    
    @address.deleter
    def address(self):
        self.__delattr__("_address")
        print("address deleted")



t = Test("ABC", 3)

# print(Test.number)
# print(t.name)
# print(t.age)

# print(dir(t))

# print(t.address)

# t.address = "IOP" # careful

# print(t.address)


# print(t.__dict__)

# del t.address

# print(t.__dict__)



# ==================================== Abstract Classes


from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def gender(self):
        pass

    @property
    @abstractmethod
    def roll_no(self):
        pass

    @roll_no.setter
    @abstractmethod
    def roll_no(self):
        pass


class Student(Person):

    _roll_no = 0

    def __init__(self):

        pass

    def age(self):
        return 20
    
    def gender(self):
        return "male"

    def name(self):
        return "ABC"

    @property
    def roll_no(self):
        return self._roll_no

# p = Person()

# stu = Student()

# print(stu)


# ================================================ Mixins
# Mixins classes
    

class WalkMixin:

    def move(self):
        print("Walking......")

class FlyMixin:

    def move(self):
        print("Flying......")


class Animal:

    pass


class Horse(Animal, WalkMixin):

    def __init__(self):

        self.move()

class Eagle(Animal, FlyMixin):

    def __init__(self):
        self.move()


h = Horse()

print(Horse.__mro__)

e = Eagle()

print(Eagle.__mro__)