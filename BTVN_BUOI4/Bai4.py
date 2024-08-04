# Viết một chương trình Python để tìm tập hợp con lớn nhất của một set sao cho tổng của các phần tử trong tập hợp con đó không vượt quá một số cho trước. Chương trình sẽ nhận đầu vào là một set có n phần tử (n > 0) và một số nguyên và trả về một set chứa các phần tử của tập hợp con lớn nhất thỏa mãn điều kiện đã nêu
# Test:
# 4                     # {1, 2, 3}
# {1, 2, 3, 4}
# 6

n= int(input())
se=set(map(int,input().split(",")))
m= int(input())
ou= set()
sum=0
for i in se:
    if(sum<m):
        sum+=i
        ou.add(i)
print(ou)


