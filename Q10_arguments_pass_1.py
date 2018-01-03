# 10. How are arguments passed in a Python method? By value or by reference?
'''

Every argument in a Python method is an Object. All the variables in Python
have reference to an Object. Therefore arguments in Python method are passed
by Reference.
Since some of the objects passed as reference are mutable, we can change
those objects in a method. But for an Immutable object like String, any change
done within a method is not reflected outside.

'''

from ctypes import *
import os.path
import sys


def test(c):
    print("test before ")
    print(id(c))
    c += 2
    print("test after +")
    print(id(c))
    return c


def printIt(t):
    for i in range(len(t)):
        print(t[i])


if __name__ == "__main__":
    a = 2
    print("main before invoke test")
    print(id(a))
    n = test(a)
    print("main afterf invoke test")
    print(a)
    print(id(a))

# id函数可以获得对象的内存地址.很明显从上面例子可以看出，将a变量作为参数传递给了test函数，
# 传递了a的一个引用，把a的地址传递过去了，所以在函数内获取的变量C的地址跟变量a的地址是一样的，
# 但是在函数内，对C进行赋值运算，C的值从2变成了4，实际上2和4所占的内存空间都还是存在的，
# 赋值运算后，C指向4所在的内存。而a仍然指向2所在的内存，所以后面打印a，其值还是2.
