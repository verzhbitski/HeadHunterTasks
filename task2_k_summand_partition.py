import sys


__author__ = 'Verzhbitski Vladislav'


def partition_number(x, y):
    if x == y or y == 1:
        return 1
    if y > x:
        return 0

    return partition_number(x - 1, y - 1) + partition_number(x - y, y)


if len(sys.argv) == 3:
    sys.stdin = open(sys.argv[1], 'r')
    sys.stdout = open(sys.argv[2], 'w')


src = raw_input()
src = src.split(' ')
n = int(src[0])
k = int(src[1])

print(partition_number(n, k))
