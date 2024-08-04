# Bài 3:
# Bài toán yêu cầu tính tổng mức độ hạnh phúc sau khi xét qua một mảng số nguyên, dựa trên hai tập hợp rời nhau A và B, với các số bạn thích (set A) và không thích (set B). Mỗi lần gặp một phần tử trong mảng:
# Nếu phần tử đó thuộc tập A, bạn thêm 1 vào mức độ hạnh phúc.
# Nếu phần tử đó thuộc tập B, bạn trừ 1 khỏi mức độ hạnh phúc.
# Nếu phần tử đó không thuộc tập A cũng không thuộc tập B, mức độ hạnh phúc không thay đổi.
# Định dạng đầu vào:
# Dòng đầu tiên chứa các số nguyên n và m được phân tách bằng một khoảng trắng.
# Dòng thứ hai chứa n số nguyên, các phần tử của mảng.
# Dòng thứ ba và thứ tư chứa m số nguyên, lần lượt là các phần tử của tập hợp A và B.
# Định dạng đầu ra:
# Xuất ra một số nguyên duy nhất, tổng mức độ hạnh phúc của bạn.
# Giải thích:
# Bạn có một mảng gồm n số nguyên và hai tập hợp A và B mỗi tập hợp chứa m số nguyên.
# Mức độ hạnh phúc bắt đầu từ 0.
# Xét từng phần tử trong mảng: nếu thuộc tập A, tăng hạnh phúc lên 1; nếu thuộc tập B, giảm hạnh phúc xuống 1; nếu không thuộc cả hai tập, mức độ hạnh phúc không thay đổi.
# Bạn cần tính và in ra tổng mức độ hạnh phúc cuối cùng.

put = list(map(int, input().split()))
n = list(map(int, input().split(",")))
A = set(map(int, input().split(",")))
B = set(map(int, input().split(",")))
sum = 0
for i in n:
    if i in A:
        sum += 1
    if i in B:
        sum -= 1
print(sum)

        