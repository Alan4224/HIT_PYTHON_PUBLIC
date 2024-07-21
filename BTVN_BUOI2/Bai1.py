# Bài 1: Tính tổng các chữ số trong một số nguyên dương
# a)Viết một chương trình yêu cầu người dùng nhập một số nguyên dương. Tính và in ra tổng các chữ số của số đó. Ví dụ: Đối với số 12345, tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15.
# b)Tính tổng các ước số của một số nguyên dương:
# Viết một chương trình yêu cầu người dùng nhập một số nguyên dương n. Tính và in ra tổng của tất cả các ước số của n. Ước số của một số là các số mà chia hết cho số đó mà không dư. Ví dụ: Ước số của 6 là 1, 2, 3, và 6.
# C)Kiểm tra tam giác:
# Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương. Kiểm tra xem 3 số đó có tạo thành tam giác hay không? Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)

# a)
import numpy as np

def a(nhap):
    nps = np.array(list(nhap), dtype=int)
    n = nps.sum()
    print("Tổng các chữ số: ",n)

nhap = input("Nhập một số: ")
a(nhap)

# b)
from math import sqrt

def b(nhap):
    sum = 0
    for i in range(1, int(sqrt(nhap)) + 1):
        if nhap % i == 0:
            sum += i
            if i != nhap // i:
                sum += nhap // i
    return sum

nhap = int(input("Nhập một số nguyên dương: "))
print("Tổng các ước số của", nhap, "là:", b(nhap))

#c)
def check(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        if a==b and b==c:
            print("Tam giác đều")
        elif a==b or b==c or c==a:
            print("Tam giác cân")
        elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 :
            print("Tam giác vuông")
        elif a**2+b**2>c**2 or a**2+c**2>b**2 or c**2+b**2>a**2 :
            print("Tam giác nhọn")
        else:
            print("Tam giác tù")
    else:
        print("Không phải tam giác")

a= int(input("Nhập cạnh tam giác: "))
b= int(input("Nhập cạnh tam giác: "))
c= int(input("Nhập cạnh tam giác: "))
check(a,b,c)