from __future__ import print_function

__author__ = 'Verzhbitski Vladislav'


def _print(*out):
    for i in out:
        print(i, sep='', end='')


def sum(x, x_sign, y, y_sign):
    tmp1 = x
    tmp2 = y
    if x_sign == '-':
        tmp1 = -tmp1
    if y_sign == '-':
        tmp2 = -tmp2

    return tmp1 + tmp2



class Polynomial:

    def __init__(self):
        self.polynomial = []

    def add_member(self, member):
        for i in range(0, len(self.polynomial)):
            if self.polynomial[i].degree < member.degree:
                self.polynomial.insert(i, member)
                return
        self.polynomial.append(member)

    def print_polynomial(self):
        start_flag = [1]
        for i in self.polynomial:
            i.out(start_flag)


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
            _print(self.sign, ' ')
            sf[0] = 0
        _print(self.coef)
        if self.degree != 0:
            _print(self.var, '^', self.degree)
        _print(" ")


def multiply_polynomial(first, second):
    result = Polynomial()

    for i in first.polynomial:
        for j in second.polynomial:
            tmp_coef = i.coef * j.coef
            if i.sign == j.sign:
                tmp_sign = '+'
            else:
                tmp_sign = '-'
            tmp_degree = i.degree + j.degree

            found = 0

            for k in result.polynomial:
                if k.degree == tmp_degree:
                    tmp_coef = sum(k.coef, k.sign, tmp_coef, tmp_sign)
                    if tmp_coef < 0:
                        k.sign = '-'
                    else:
                        k.sign = '+'

                    k.coef = abs(tmp_coef)
                    found = 1
                    break

            if not found:
                tmp = Member(tmp_coef, tmp_sign, i.var, tmp_degree)
                result.add_member(tmp)

    return result


first = Member(5, '-', 'x', 2)
second = Member(11, '+', 'x', 6)

pol = Polynomial()
pol.add_member(first)
pol.add_member(second)
pol.print_polynomial()
print()
first = Member(12, '+', 'x', 10)
second = Member(17, '-', 'x', 5)
pol1 = Polynomial()
pol1.add_member(first)
pol1.add_member(second)
pol1.print_polynomial()
print()
pol = multiply_polynomial(pol1, pol)
# pol.print_polynomial()
# pol.simplification()
pol.print_polynomial()
