#!/usr/bin/python
# -*- coding:utf-8 -*-


class MyBaseClass(object):
    def __init__(self):
        print "base class"
        

class MyClass(MyBaseClass):
    def __new__(self):
        print "new"
        return MyBaseClass()
    def __init__(self):
        print "init"

class MyAClass(object):
    foo = 2
    far = { 2:'a'}
    fae = [ 4,5,6]
    def __init__(self):
        print "init"
        self.fei = 'f'
    def show(self):
        print "show"
        print self.foo
    def add(self):
        print "add"
        self.foo += 1

myIn = MyClass()
print type(myIn)
myA = MyAClass()
print type(myA)
myA.fei = 'e'
print myA.fei
myA.show()
print myA.foo
print myA.far
myA.far[2] = 'c'
myA.fae += [7,8]
MyAClass.foo = 5
print MyAClass.foo
print MyAClass.far
print myA.foo
print myA.fae
