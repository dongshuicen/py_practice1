#!/usr/bin/python3

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def print1(self):
        print(self.__class__)

x = Complex(3.0, -4.5)
print(x.r, x.i)
x.print1()