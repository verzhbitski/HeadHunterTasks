from __future__ import print_function
import re

__author__ = 'Verzhbitski Vladislav'

var = 'x'


def _print(*out):
    for i in out:
        print(i, sep='', end='')


class Polynomial:

    def __init__(self):
        self.polynomial = []

    def print_polynomial(self):
        start_flag = [1]
        for i in self.polynomial:
            i.out(start_flag)

    def add_member(self, member):
        for i in range(0, len(self.polynomial)):
            if self.polynomial[i].degree == member.degree:
                self.polynomial[i].coef += member.coef
                return
            if self.polynomial[i].degree < member.degree:
                self.polynomial.insert(i, member)
                return

        self.polynomial.append(member)


class Member:

    def __init__(self, coefx=1, varx='', degreex='0'):
        self.coef = coefx
        self.var = varx
        self.degree = degreex

    def out(self, sf):
        if self.coef == 0:
            return
        if (sf[0] == 1) and (self.coef > 0):
            sf[0] = 0
        else:
            if self.coef > 0:
                _print('+ ')
            else:
                _print('- ')
            sf[0] = 0
        _print(abs(self.coef))
        if self.degree != 0:
            _print(self.var)
            if self.degree != 1:
                _print('^', self.degree)
        _print(" ")


def sum_polynomial(first, second):
    result = first

    for i in second.polynomial:
        found = 0
        for j in result.polynomial:
            if i.degree == j.degree:
                found = 1
                j.coef += i.coef

        if not found:
            result.add_member(i)

    return result


def res_polynomial(first, second):
    result = first
    for i in second.polynomial:
        found = 0
        for j in result.polynomial:
            if i.degree == j.degree:
                found = 1
                j.coef -= i.coef

        if not found:
            i.coef *= -1
            result.add_member(i)

    return result


def multiply_polynomial(first, second):
    result = Polynomial()
    tmp_var = 'x'

    for i in first.polynomial:
        for j in second.polynomial:
            tmp_coef = i.coef * j.coef
            tmp_degree = i.degree + j.degree
            tmp = Member(tmp_coef, tmp_var, tmp_degree)
            result.add_member(tmp)

    return result


def is_degree(x):
    if x == '^':
        return 1
    else:
        return 0


def read_sign(x):
    if x == '-':
        return -1
    else:
        return 1


def parse_polynomial(src):
    src = re.sub('([\+\-])\s+', '\g<1>', src)
    # print(src)
    result = Polynomial()
    member_list = re.split('\s+', src)
    # tmp_var = re.search('[a-z]', src)
    # tmp_var = tmp_var.group(0)
    for i in member_list:
        tmp = re.findall('([-\+])?(?:([\d]+)(?:([a-z])(?:(?:(?:\^))([\d]+))?)|([\d]+))', i)
        # print(tmp)

        if tmp[0][0] == '-':
            tmp_sign = -1
        else:
            tmp_sign = 1

        if tmp[0][4] != '':
            tmp_degree = 0
            tmp_coef = tmp_sign * int(tmp[0][4])
        else:
            tmp_coef = tmp_sign * int(tmp[0][1])
            if tmp[0][3] == '':
                tmp_degree = 1
            else:
                tmp_degree = int(tmp[0][3])

        tmp_member = Member(tmp_coef, var, tmp_degree)
        result.add_member(tmp_member)
    return result


src = raw_input()
pol = parse_polynomial(src)
pol.print_polynomial()
print()
src2 = raw_input()
pol1 = parse_polynomial(src2)
pol1.print_polynomial()
print()

pol1 = res_polynomial(pol1, pol)
pol1.print_polynomial()

# first = Member(5, 'x', 6)
# second = Member(-11, 'x', 6)
#
# pol = Polynomial()
# pol.add_member(first)
# pol.add_member(second)
# pol.print_polynomial()
# print()
# first = Member(-12, 'x', 7)
# second = Member(17, 'x', 5)
# pol1 = Polynomial()
# pol1.add_member(first)
# pol1.add_member(second)
# pol1.print_polynomial()
# print()
# pol = res_polynomial(pol, pol1)
# # pol.print_polynomial()
# # pol.simplification()
# pol.print_polynomial()
