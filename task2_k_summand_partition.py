__author__ = 'Verzhbitski Vladislav'


def partition_number(x, y):
    if x == y or y == 1:
        return 1
    if y > x:
        return 0

    return partition_number(x - 1, y - 1) + partition_number(x - y, y)

n = int(input())
k = int(input())

print(partition_number(n, k))
