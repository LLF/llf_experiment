#!/usr/bin/python

class P1(object):
    def foo(self):
        print 'called P1-foo'


class P2(object):
    def foo(self):
        print 'called P2-foo'

    def bar(self):
        print 'P2-bar'

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print 'C2-bar'

class GC(C1,C2):
    pass

class C(object):
    a = 'b'
    def __getattribute__(self,name):
        print "here is name",name


ins = GC()
ins.foo()
ins.bar()
print GC.__mro__
c1 = C()
c1.a
print c1.__slots__
print C.__dict__
