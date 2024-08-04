# Bài 1:
# Cho một tuple gồm n phần tử kiểu xâu ký tự nhưng các ký tự đều là các con số từ 0 tới
# 9. Hãy chuyển đổi tuple đó để thu được tuple mới gồm phần tử kiểu số tương ứng.
# Tính trung bình cộng các phần tử trong tuple thu được.

n = tuple(input("Nhập tuple: ").split(','))
n = tuple(map(lambda x: int(x.strip("'")), n))
print("Trung bình cộng: ", sum(n) / len(n))