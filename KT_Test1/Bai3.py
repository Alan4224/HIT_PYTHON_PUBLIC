# Bài 3:(20 điểm):
# Sau buổi kiểm tra của lớp Python Public hôm nay, leader Mạnh Hùng siêu cấp đẹp trai đã có danh sách số lượng thành viên tham gia, cùng với tên và số điểm của từng người. Không vì lý do gì cụ thể, nhưng leader Đào Chiến muốn thử thách Hùng bằng cách yêu cầu tìm tên của thành viên có số điểm thấp nhì. Tuy nhiên, danh sách điểm không được sắp xếp, và Hùng lại có lịch đi chơi cùng bạn “nào đó”  nên không thể tìm ra một cách nhanh chóng. Vì vậy, hãy giúp leader của chúng ta giải quyết vấn đề này!

# Đầu vào:
# Dòng đầu là số lượng các bạn tham gia kiểm tra
# Các dòng sau bao gồm tên và điểm của bạn đó
# Đầu ra:
# In ra tất cả tên của các bạn có số điểm thỏa mãn
# Test:

# Input
# Output
# 5
# Khánh 73
# Hoàng 51
# Phương 58
# Duy 93
# Hòa 81


# Phương



n = int(input())
hungDict = {}
for i in range(n):
    key, value = input().split()
    hungDict[key] = value
out=set(hungDict.values())
out=list(out)
find = out[-2]
for key, value in hungDict.items():
    if value == find:
        print(key)

