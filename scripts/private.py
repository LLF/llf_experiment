#!/bin/usr/python
# -*- coding:utf-8 -*-


class test(object):
    __foo = "abc"
    _bar = '123'

    def show(self):
        print 'show'
        print self.__foo

class testSon(test):
    __foo = "cba"
    
    def fshow(self):
        print self.__foo

if __name__ == "__main__":
    t1 = test()
    print t1._test__foo
    t2 = testSon()
    t2.fshow()
    print t2._bar
