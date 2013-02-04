#!/usr/bin/python
# -*- coding:utf-8 -*-

def foo(x):
    print(x)
class StaticClass(object):
    def __init__(self,function):
        print("__init__() called")
        self.f = function
    def __get__(self, instance, owner):
        print("__get__() called")
        print("INFO: self = %s, instance = %s, owner = %s" % (self,instance,owner))
        return self.f

class MyClass(object):
    method = StaticClass(foo)


if __name__ == "__main__":
    ins = MyClass()
    print("ins = %s, Class = %s" % (ins, MyClass))
    print("ins.method = %s, MyClass.method = %s" % (ins.method, MyClass.method))
    ins.method('a')
    MyClass.method('b')
