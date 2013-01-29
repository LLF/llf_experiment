#!/usr/bin/python


def decorator_fun(arg1,arg2):
    print 'decorator'
    def inner_fun(func):
        print 'inner'
        print arg1,arg2
        return change_fun
    def change_fun(outter_arg):
        print 'change'
        print outter_arg

    return inner_fun



@decorator_fun('foo','bar')
def func(arg1):
    print 'func'
    print 'arg1:',arg1




func('llf')

def decorator_fun2(arg1):
    print '2'
    def inner_fun(func):
        print 'inner 2'
        print arg1
        return func
    return inner_fun

def func2(arg1):
    print 'func2'
    print 'arg1:',arg1

#fun2 = decorator_fun2('de2')(func2)
#fun2('ww')
