from __future__ import print_function
import re

__author__ = 'Verzhbitski Vladislav'


expression = raw_input()
var = re.search('[a-z]', expression)
var = var.group(0)


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

    def __init__(self, coefx=1, varx='', degreex=0):
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

        if not ((abs(self.coef) == 1) and (self.degree != 0)):
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

    for i in first.polynomial:
        for j in second.polynomial:
            tmp_coef = i.coef * j.coef
            tmp_degree = i.degree + j.degree
            tmp = Member(tmp_coef, var, tmp_degree)
            result.add_member(tmp)

    return result


def parse_polynomial(src):
    result = Polynomial()
    tmp = re.findall('(?:([\d]*)(?:([a-z])(?:(?:(?:\^))([\d]+))?)|([\d]+))', src)

    if tmp[0][3] != '':
        tmp_degree = 0
        tmp_coef = int(tmp[0][3])
    else:
        if tmp[0][0] != '':
            tmp_coef = int(tmp[0][0])
        else:
            tmp_coef = 1
        if tmp[0][2] == '':
                tmp_degree = 1
        else:
            tmp_degree = int(tmp[0][2])

    tmp_member = Member(tmp_coef, var, tmp_degree)
    result.add_member(tmp_member)
    return result


def normalize(src):
    src = re.sub('\s+', '', src)
    src = re.sub('\)\(', ')*(', src)
    src = re.sub('([\w])\(', '\g<1>*(', src)
    src = re.sub('\)(\w)', ')*\g<1>', src)
    return src


class Exp:

    def __init__(self):
        self.left = 0
        self.right = 0
        self.value = ''

    def write(self):
        if self.left == 0 and self.right == 0:
            _print(self.value)
            return
        else:
            _print('(')
            self.left.write()
            _print(self.value)
            self.right.write()
            _print(')')


def search_close_bracket(src, start):
    open_b = 1
    for i in range(start, len(src)):
        if src[i] == '(':
            open_b += 1
        elif src[i] == ')':
            open_b -= 1

        if open_b == 0:
            return i

    return -1


def clear(src):
    if search_close_bracket(src, 1) == len(src) - 1:
        return clear(src[1: -1])
    else:
        return src


def is_member(src):
    for i in src:
        if i in ('+', '-', '(', '*', ')'):
            return False

    return True


def parse(src):
    result = Exp()
    first_operation = False
    mul_position = 0
    src = clear(src)
    i = 0
    if not is_member(src):
        while i < len(src):
            if src[i] == '(':
                i = search_close_bracket(src, i + 1)
            elif src[i] in ('+', '-'):
                if src[i] == '-' and i == 0:
                    result.left = parse('0')
                    result.right = parse(src[i + 1:])
                    result.value = src[i]
                    first_operation = True
                else:
                    result.left = parse(src[:i])
                    result.right = parse(src[i + 1:])
                    result.value = src[i]
                    first_operation = True
            elif src[i] == '*':
                mul_position = i

            i += 1

        if not first_operation:
            result.left = parse(src[0: mul_position])
            result.right = parse(src[mul_position + 1:])
            result.value = '*'
    else:
        result.value = src

    return result


def compute(exp):
    if exp.left == 0 and exp.right == 0:
        exp = parse_polynomial(exp.value)
        return exp

    if exp.value == '*':
        exp = multiply_polynomial(compute(exp.left), compute(exp.right))
        return exp
    elif exp.value == '+':
        exp = sum_polynomial(compute(exp.left), compute(exp.right))
        return exp
    elif exp.value == '-':
        exp = res_polynomial(compute(exp.left), compute(exp.right))
        return exp


expression = normalize(expression)
expression = parse(expression)
expression = compute(expression)
expression.print_polynomial()
