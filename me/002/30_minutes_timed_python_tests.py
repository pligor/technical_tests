#!/usr/bin/env python
from __future__ import division
import numpy as np
import os

def question_1():
    # What does the *args and **kwargs in a function definition do?
    def func(*args):
        for arg in args:
            print arg

    func('test1', 'test2', "test3")
    somelist = ['test1', 'test2', "test3"]
    func(*somelist)

    def func2(**kwargs):
        for k, v in kwargs.iteritems():
            print k
            print v

    func2(hello = "3", home = "4")

question_1()
print

print "question 2"


class myClass(object):
    def __init__(self, x):
        super(myClass, self).__init__()
        self.__x = x

    @property
    def x(self):
        return self.__x

def question_2():
    # Define a class
    # The class should have a object property "x"
    # The property "x" should have a getter, you should only be able to set "x"
    # when you create an instance of the class.

    obj = myClass("question test")
    print obj.x
    #print obj.__x #not working

question_2()
print

print "question 3"

def question_3():
    # Write a generator that will cycle through a range from an initial value and stop at an end value
    # The generator should only return even values.
    # eg. get_even_values(1, 5) -> [2, 4]
    def get_even_values(low, high):
        mylist = []
        for i in range(low, high+1):
            if i % 2 == 0:
                mylist.append(i)

        return mylist

    def get_even_values2(low, high):
        lowbound = low if (low % 2 == 0) else (low+1)
        highbound = high if (high % 2 == 0) else (high-1)
        return range(lowbound, highbound+1, 2)

    print get_even_values(1, 6)
    print get_even_values2(1, 6)

    print get_even_values(1, 5)
    print get_even_values2(1, 5)

    print get_even_values(2, 5)
    print get_even_values2(2, 5)

    print get_even_values(2, 6)
    print get_even_values2(2, 6)


question_3()
print

print "question 4"

#import property

def question_4():
    # How would you sort a list of objects of the same type (Use the class defined in question 2)?
    # What functions do you need to implement on the class for sorting?

    thelist = [myClass(10), myClass(3), myClass(8)]

    def get_x(obj):
        return obj.x

    sortlist = sorted(thelist, key=get_x)

    return [v.x for v in sortlist]

print question_4()

