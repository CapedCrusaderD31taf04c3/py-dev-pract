

def i_am_method():

    return "I am method from module"


class Module:

    def __init__(self):

        pass

    @classmethod
    def say_hi(self):

        return "Hi from Module"

    @staticmethod
    def i_am_static_hi():

        return "Hi From Static"
