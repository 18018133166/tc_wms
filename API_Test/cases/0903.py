# import time
#
#
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start_time=time.time()
#         func(*args, **kwargs)
#         end_time=time.time()
#         return end_time-start_time
#     return wrapper
#
# l=list(range(0,5,2))
# l2=[1,2]
# l.extend(l2)
# print(l)
# @timmer
# def test_a(l):
#     new_list=[]
#     for i in l:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# @timmer
# def test_b(l):
#     new_list=set(l)
#     return new_list
#
# print(test_a(l))
# print(test_b(l))
# import random
# import timeit
#
#
# def randomList(n):
#     '''返回一个长度为n的整数列表，数据范围[0,1000) '''
#     iList = []
#     for i in range(n):
#         iList.append(random.randrange(1000))
#     return iList
#
# iList=[2,51,8,1,3,33,13]
# def quickSort(iList):
#     if len(iList) <= 1:
#         return iList
#     left = []
#     right = []
#     for i in iList[1:]:
#         print(f'iList[1:]={iList[1:]}')
#         print(f'i={i}')
#         if i <= iList[0]:
#             print(f'{i} <= {iList[0]}：{i <= iList[0]}')
#             left.append(i)
#             print(f'left={left}')
#         else:
#             print(f'{i} <= {iList[0]}：{i <= iList[0]}')
#             right.append(i)
#             print(f'right={right}')
#     print(f'for循环结束left:{left}')
#     print(f'for循环结束right:{right}')
#     print(f'for循环结束iList:{iList}')
#     return quickSort(left) + [iList[0]] + quickSort(right)
# print(quickSort(iList))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xiaoke


def bubble_sort(alist):
    # 结算列表的长度
    n = len(alist)
    # 外层循环控制从头走到尾的次数
    for j in range(n - 1):
        print(f'j in range(n - 1):{range(n - 1)}')
        print(f'j:{j}')
        # 用一个count记录一共交换的次数，可以排除已经是排好的序列
        count = 0
        # 内层循环控制走一次的过程
        for i in range(0, n - 1 - j):
            print(f'i in range(0, n - 1 - j):{range(0, n - 1 - j)}')
            print(f'i:{i}')
            # 如果前一个元素大于后一个元素，则交换两个元素（升序）
            print(f'{alist[i]} > {alist[i + 1]}:{alist[i] > alist[i + 1]}')
            if alist[i] > alist[i + 1]:
                # 交换元素
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # 记录交换的次数
                print(f'alist={alist}')
                count += 1
                print(f'count={count}')
        # count == 0 代表没有交换，序列已经有序
        if 0 == count:
            break


if __name__ == '__main__':
    alist = [3,2,4,1]
    bubble_sort(alist)
    print(f"新列表为：{alist}")


