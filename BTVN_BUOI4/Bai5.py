# Bài 5:
# Tạo một mảng xâu a chứa n phần tử (mảng mà mỗi phần tử là 1 xâu ký tự nhập từ bàn phím).
# - Hãy tạo một tuple b từ mảng a với các phần tử của tuple được lấy lần lượt trong a và in ra màn hình.
# - Một phần tử của b được gọi là có dạng số nếu chúng chứa toàn các con số (ví dụ: ‘123’, ‘030’ là dạng số; ‘a13’, ‘hello’ là không phải dạng số). Hãy đếm xem có bao nhiêu phần tử trong b có dạng số.

a=list(input().split(","))
print(a)
b=tuple(a)
print(b)
coun=0
for i in b:
    if i.isdigit():
        coun+=1
print(coun)