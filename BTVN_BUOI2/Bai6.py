# Bài 6: Nhập vào 1 số n. In ra tất cả các số hoàn hảo từ 1 đến n. ( Số hoàn hảo là số mà tổng các ước của nó (không tính chính nó) bằng chính nó ).
from math import sqrt

def perf(a):
    sum = 0
    for i in range(1, int(sqrt(a)) + 1):
        if a % i == 0:
            sum += i
            if i != 1 and i != a // i:
                sum += a // i
    return sum == a

def out(n):
    for i in range(1, n + 1):
        if perf(i):
            print(i)

n = int(input("Nhập số lượng: "))
out(n)