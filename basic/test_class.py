#!/bin/env python

class Sorter:
    def __init__(self, name):
        self.name=name
    def sort(self):
        print(self.name+" sort method")

class QuickSorter(Sorter):
    def __init__(self, name):
        self.name=name
    def sort(self):
        print(self.name+"rewrite sort from QuickSorter")

class ChooseSorter(Sorter):
    pass

class Test():
    pool = None
    def __init__(self,name):
        if self.pool is None:
            self.pool = name
            print self.pool

sm=Sorter("origin")
sm.sort()

sm=ChooseSorter("choose")
sm.sort()

sm=QuickSorter("quick")
sm.sort()

test=Test('hi')
