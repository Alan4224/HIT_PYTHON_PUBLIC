# Bài 1:(25 điểm):bạn 
# Cho một tuple, nhiệm vụ của các là đưa ra các số mà số lần xuất hiện của nó có trong tuple là bội của 5 nhưng số đó không là bội của 10. Kết quả có thể in theo thứ tự bất kì.
# Đầu vào: 
# Một dòng chứa các số nguyên, các số cách nhau bởi dấu cách
# Đầu ra: 
# In ra các số thỏa mãn yêu cầu.
# Test:

# Input
# Output
# 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 3 3 3 4 4 4 4 4
# 2 4



put = tuple(map(int, input().split()))
lis = []
for i in range(2, len(put)):
    if put[i] != put[i-1]:
        if put.count(put[i]) % 5 == 0 and  put.count(put[i])% 10 != 0:
            lis.append(put[i])
print(lis)

