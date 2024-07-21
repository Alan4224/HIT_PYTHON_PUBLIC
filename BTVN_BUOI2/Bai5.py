# Bài 5: Nhập vào 1 số n. Viết chương trình in ra tất cả các số Armstrong bậc 3 từ 1 đến n. (Số Armstrong bậc 3 là số mà tổng lập phương của các chữ số của nó bằng chính nó)

import numpy as np

def is_as(a):
    nps= np.array(list(str(a)),dtype=int)
    sum=0
    for i in nps:
       sum+=i**3 
    if sum==a:
        return True
    else: 
        return False
    
def ast(n):
    for i in range(1,n+1):
        if is_as(i):
            print(i)

n = int(input("Nhập số lượng: "))
ast(n)
