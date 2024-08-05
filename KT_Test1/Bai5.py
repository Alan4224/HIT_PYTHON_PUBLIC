# Bài 5:(10 điểm)
# Bạn được cho một dãy số a1,a2,…,an. Một dãy số b1,b2,…,bn được gọi là "tốt" nếu nó thỏa mãn tất cả các điều kiện sau:
# bi​ là một số nguyên dương với i=1,2,…,n;
# bi ≠ai với i=1,2,…,n;
# b1 < b2 < … < bn​.
# Tìm giá trị nhỏ nhất của bn
# Đầu vào:
# Mỗi test case gồm hai dòng:
# Dòng đầu tiên chứa một số nguyên n (1 ≤ n ≤ 100) — số lượng phần tử trong dãy.
# Dòng thứ hai chứa n số nguyên a1,a2,…,an​ (1 ≤ ai​ ≤ 10^9).
# Đầu ra:
# Đối với mỗi test case, in ra một số nguyên — giá trị nhỏ nhất của bn.

# Input
# Output
# 5
# 1 3 2 6 7

# 8





n=int(input())
lis=list(map(int, input().split()))
lis=set(lis)
lis=list(lis)
print(lis[-1]+1)