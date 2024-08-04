# Bài 2:
# Khởi tạo hai tập hợp (set), trong đó tập A chứa các mã sinh viên đăng ký hoc tiếng
# Anh tại bàn tiếp nhận số 1, tập B là các mã sinh viên đăng ký học tại bàn tiếp nhận số
# 2. In thông tin hai tập hợp lên màn hình.
# - Cho biết có sinh viên nào đăng ký học tại cả hai bàn hay không.
# - Cho biết danh sách tổng hợp của các sinh viên đã đăng ký của cả hai bàn.
# - Cho biết danh sách các sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn
# 2.

a={"SV001","SV002","SV003","SV004","SV005"}
b={"SV003","SV004","SV005","SV006","SV007"}
print(a&b)
print(a|b)
print(a - b)