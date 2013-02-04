#!/usr/bin/python
# coding = utf-8


def simpleGen():
    var = 2
    yield var+1
    var += 1
    print (yield var+1)
    print '333'
    var += 1
    yield 'here'
    return 

myG = simpleGen()

myL = list(myG)
print myL

myG.next()
myG.next()
myG.next()


def counter(start=0):
    count = start
    while True:
        val = (yield count) 
        print 'count:', count
        if val is not None:
            print 'has val'
            count = val
        else:
            print 'no val'
            count += 1

count = counter(5)
print count.next()
print count.next()
count.send(9)
print count.next()
print count.next()
