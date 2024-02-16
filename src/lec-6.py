

import asyncio
import time

# Asynchronous
# ================================================================

# def power(number):

#     print("Inside Power .....")

#     time.sleep(5)

#     print("Calculating Power ......")

#     value = number * number * number

#     print(value)

#     return value

# def square(number):

#     print("Inside Square .....")

#     time.sleep(2)

#     print("Calculating Square ......")

#     value = number * number

#     print(value)

#     return value



# def main():

#     returned_values = power(2), square(2)

#     print(type(returned_values))
#     print(returned_values)


# if __name__ == '__main__':

#     main()


# ================================================================


# async def power(number):

#     print("Inside Power .....")

#     await asyncio.sleep(5)

#     print("Calculating Power ......")

#     value = number * number * number

#     print(value)

#     return value

# async def square(number):

#     print("Inside Square .....")

#     await asyncio.sleep(2)

#     print("Calculating Square ......")

#     value = number * number

#     print(value)

#     return value



# async def main():

#     returned_values = await asyncio.gather(power(2), square(2))

#     print(type(returned_values))
#     print(returned_values)


# if __name__ == '__main__':

#     asyncio.run( main() )

# ================================================================
