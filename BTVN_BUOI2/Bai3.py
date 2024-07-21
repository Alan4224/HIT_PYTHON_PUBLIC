# Bài 3: Tính các tổng sau:
# a) S(n) = 1 - 2 + 3 - 4 + 5 + .... + (2*n + 1)
# b) S(n) = 1 + ½ + ⅓ + ¼ +.....+1/n
# c) Biện luận nghiệm của phương trình bậc 2 một ẩn

def a(n):
    sum=0
    for i in range(1,2*n+2):
        if(i%2!=0):
            sum+=i
        else:
            sum-=i
    return sum
def b(n):
    sum=0
    for i in range(1,n):
        sum+=1/i
    return sum

from math import sqrt

def c1(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                print("Vô số nghiệm")
            else:
                print("Vô nghiệm")
        else:
            print("Có ngiệm duy nhất: ",-c/b)
    else:
        delta= b**2-4*a*c
        if delta<0:
            print("Vô nghiệm")
        elif delta==0:
            print("Có nghiệm kép: ",-b/(2*a))
        else:
            print("Có 2 nghiệm: ",(-b+sqrt(delta))/(2*a),"và",(-b-sqrt(delta))/(2*a))

n=int(input("Nhập số n"))
print(a(n))
print(b(n))
a=int(input("Nhập số a"))
b=int(input("Nhập số b"))
c=int(input("Nhập số c"))
c1(a,b,c)