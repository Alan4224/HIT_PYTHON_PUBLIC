# Bài 1:
# Nhập vào một list có N phần tử là số nguyên.(N nhập từ bàn phím):
# Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list.
# Thay thế phần tử từ vị trí 2 -> 7 trong list thành [8, 5, 4, 0, 1, 3].
# Sử dụng list sau khi thay thế để giải quyết các bài toán tiếp theo.
# Tìm số lớn nhất, và nhỏ nhất trong list.
# Nhập một số Y tùy chọn từ bàn phím. Chèn số Y vào đầu list.
# Sau khi chèn số Y, kiểm tra các số trong list có sắp xếp theo thứ tự tăng dần hay giảm dần không. Nếu sắp xếp theo tăng dần thì in ra màn hình “TĂNG”, còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIÁM”, nếu không tăng không giảm thì in “NO”.
# Tạo một list mới có N phần tử. Các phần tử sẽ có vị trí từ 1 -> N. Với mỗi phần tử ở vị trí i (1 <= i <= N) giá trị của nó là tổng i phần tử đầu tiên của list cũ.
# # Tạo một list mới [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000] và sắp xếp nó theo thứ tự tăng dần của giá trị, và sắp xếp nó theo sự tăng dần của giá trị tuyệt đối.
# avccccc
#
N=int(input("Nhập N: "))
print("Nhập list: ")
lst=[int(input()) for _ in range(N)]
#
X=int(input("Nhập X: "))
print("{} xuất hiện trong mảng {} lần".format(X,lst.count(X)))
#
if N>=8:
    lst1=lst[8:]
else:
    lst1=[]
lst=lst[0:2]
lst.extend([8, 5, 4, 0, 1, 3])
lst.extend(lst1)
#
print("Số lớn nhất trong list: ",max(lst))
print("Số nhỏ nhất trong list: ",min(lst))
#
Y=int(input("Nhập Y: "))
lst.insert(0,Y)
k = lst.copy()
k.sort()
if lst == k:
    print("TĂNG")
elif lst == k[::-1]:
    print("GIẢM")
else:
    print("NO")
#
Z=lst.copy()
for i in range(len(Z)):
    Z[i]=sum(lst[0:i+1])
print(Z)
#
A=[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
A.sort()
print(A)
#
for i in range(len(A)):
    A[i]=abs(A[i])
A.sort()
print(A)   
    