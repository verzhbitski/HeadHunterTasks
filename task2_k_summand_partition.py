__author__ = 'Verzhbitski Vladislav'


def P(n, k):
    if n == k or k == 1:
        return 1
    if k > n:
        return 0

    return P(n - 1, k - 1) + P(n - k, k)

n = int(raw_input())
k = int(raw_input())

print(P(n, k))
