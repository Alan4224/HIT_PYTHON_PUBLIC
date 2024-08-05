# Bài 4:(20 điểm):
# Nhập từ bàn phím một danh sách (list) gồm các phần tử là các chuỗi ký tự. In ra màn hình một danh sách mới gồm các phần tử là các số và chuỗi ký tự được tách ra từ các chuỗi ban đầu, và các phần tử này không được lặp lại.
# Đầu vào:
# Một dòng duy nhất chứa danh sách đầu vào, các phần tử được ngăn cách bởi dấu cách.
# Đầu ra:
# Một danh sách kết quả chứa các phần tử đã được tách ra và không lặp lại theo thứ tự bất kì
# Test:

# Input
# Output
# neihc5201 abc123
# ['3', 'i', 'e', 'h', 'c', '2', '0', '5', '1', 'n', 'b', 'a']



iput=list(input().split(','))
for i in range(len(iput)):
    iput[i]=list(iput[i])
print(iput)
oput=[char for word in iput for char in word]
print(oput)