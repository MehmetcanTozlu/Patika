print('*****************Soru-1*********************')


def flatten(arr):

    for i in arr:
        if isinstance(i, list):
            flatten(i)
        else:
            birlestirilmisDizi.append(i)
    return birlestirilmisDizi


l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]


birlestirilmisDizi = []
flatten(l)
print(birlestirilmisDizi)

print('*****************Soru-2*********************')

arr = [[1, 2], [3, 4], [5, 6, 7]]


def testCevir(arr):
    for i in arr:
        a.append(i[::-1])
    a.reverse()
    return a


a = []
testCevir(arr)
print(a)
