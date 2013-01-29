#!/usr/bin/python
from random import randint, choice
from operator import add, sub

ops = {'+': add, '-': sub}
MAXTRIES = 2

def rand_cal():
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    op = choice("+-")
    answer = ops[op](*nums)
    prompt = '%d %s %d = ' % (nums[0], op, nums[1])
    times = 0
    while times < MAXTRIES:
        try:
            if int(raw_input(prompt)) == answer:
                print 'correct'
                break
            print 'incorrect...please try again'
            if times == 0:
                print 'one more chance'
            times += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input...plaese try again'
    else:
        print 'answer is %d' % answer

def main():
    while True:
        rand_cal()
        try:
            option = raw_input('Again? [y]').lower()
            if option and option[0] == 'n':
                print 'bye'
                break
        except(KeyboardInterrupt, EOFError):
            print 'bye'
            break

if __name__=='__main__':
    main()

