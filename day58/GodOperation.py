"""
那些操作2
"""

# 字典按value排序并返回新字典
d = {'a': 12, 'b': 50, 'c': 1, 'd': 20}
# 使用python内置函数sorted排序:
d = dict(sorted(d.items(), key=lambda item: item[1]))
print(d)

# 删除list里的重复元素，并保证元素顺序不变


def del_duplicated(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b


a = [3, 2, 2, 2, 1, 6, 3]
print(del_duplicated(a))

# 找出两个列表的相同元素和不同元素


def ana(a, b):
    aset, bset = set(a), set(b)
    same = aset.intersection(bset)
    differ = aset.difference(bset).union(bset.difference(aset))
    return same, differ


a = [3, 2, 2, 2, 1, 3]
b = [1, 4, 3, 3, 2, 2, 3]
print(ana(a, b))
