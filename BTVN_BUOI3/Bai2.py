# Bài 2:
# Cho một list a gồm k phần tử(a và k nhập từ bàn phím). Nhập vào hai số nguyên n, m là số dòng và số cột của một ma trận.
# Hãy xây dựng ma trận X(n × m) với các phần tử lần lượt lấy ra từ list ở trên (nếu có
# thể).
# Ví dụ: a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6], k = 18. Giả sử n = 3 và m =
# 4, ma trận x(3 × 4) thu được có dạng [[1, 2, 4, 3], [5, 4, 3, 6], [1, 4, 2, 7]]. Nhưng với
# n = 3, m = 7 ta không thể xây dựng được ma trận. In ra kết quả nếu có thể, không thì in ra “NO”

a=list(map(int,input("Nhập list a: ").split()))
n=int(input("Nhập n: "))
m=int(input("Nhập m: "))
if m*n > len(a):
    print("NO")
else:
    mt=[]
    index=0
    for i in range(n):
        hang=[]
        for j in range(m):
            hang.append(a[index])
            index+=1
        mt.append(hang)
    print(mt)