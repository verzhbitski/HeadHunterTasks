__author__ = 'Verzhbitski Vladislav'


def P(n, k):
    if n == k or k == 1:
        return 1
    if k > n:
        return 0

    return P(n - 1, k - 1) + P(n - k, k)

n = 4
k = 4
print(P(n, k))
