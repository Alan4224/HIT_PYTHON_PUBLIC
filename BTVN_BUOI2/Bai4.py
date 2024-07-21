# Bài 4:  Dãy số Fibonacci
# Hãy viết chương trình tìm n số Fibonacci đầu tiên.
# Quy luật của dãy số Fibonacci: số tiếp theo bằng tổng của 2 số trước, 2 số đầu tiên của dãy số là 0, 1. Ví dụ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fb(n):
    fi=[0]*(n+1)
    fi[0]=1
    fi[1]=1
    print(fi[0])
    print(fi[1])
    for i in range (2,n+1):
        fi[i]=fi[i-1]+fi[i-2]
        print(fi[i])

n=int(input("Nhập số lượng: "))
print(n,"số Fibonacci đầu tiên")
fb(n)