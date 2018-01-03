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


def test(list2):
    print("test before ")
    print(id(list2))
    list2[1] = 30
    # list2=['1','2']   # 由于是赋值操作所以这是一个新的对象,这个变量重新赋予了一个地址，覆盖了原本列表的地址，
                        # 这个时候，lst2列表的内存id就发生了改变。
    print("test after +")
    print(id(list2))
    return list2


def printIt(t):
    for i in range(len(t)):
        print(t[i])


if __name__ == "__main__":
    list1 = ["loleina", 25, 'female']
    print("main before invoke test")
    print(id(list1))
    list3 = test(list1)
    print("main afterf invoke test")
    print(list1)
    print(id(list1))

# Python参数传递采用的肯定是“传对象引用”的方式。这种方式相当于传值和传引用的一种综合。
# 如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。
# 如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。