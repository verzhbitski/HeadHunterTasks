from __future__ import print_function

__author__ = 'Verzhbitski Vladislav'


start_flag = [1]

class Member:

    sign = '+'
    coef = 1
    var = ''
    degree = 0

    def __init__(self, coefx, signx, varx, degreex):
        self.coef = coefx
        self.sign = signx
        self.var = varx
        self.degree = degreex

    def out(self, sf):
        if (sf[0] == 1) and (self.sign == '+'):
            sf[0] = 0
        else:
            print(self.sign, ' ', sep='', end='')
        print(self.coef, sep='', end='')
        if self.var != '':
            print(self.var, sep='', end='')
        if self.degree != 0:
            print('^', self.degree, sep='', end='')

first = Member(5, '-', 'y', 6)
first.out(start_flag)
#first.out()

#src = raw_input()
#src = src.replace(' ', '')
#print(src)
