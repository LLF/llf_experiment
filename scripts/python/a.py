#!/usr/bin/python



class test(object):
    string = ''
    def __init__(self, string):
        print 'init'
        self.string = string

    def __add__(self, obj):
        print 'add'
        return self

a = test('2')

b = test('4')

c = a + b




from functools import wraps
def first():
    print 'fir'
    return 1

def second():
    print 'sec'
    return 2

f = wraps(second)(first)
print f()
