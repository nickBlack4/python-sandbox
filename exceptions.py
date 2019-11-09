# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("blah")

# else:
#     print("No exceptions were thrown")
# finally:
#     # the perfect place to close files, database connections, network connections and so on
#     file.close()

from timeit import timeit
# can calculate the execution time of some python code


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass 
    # cannot have an empty except block
"""
# number is num of times we want to execute code
# first code is label
print("first code=", timeit(code1, number=10000))
