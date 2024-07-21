# Bài 7: Viết một chương trình nhận vào một số N từ người dùng và in ra tất cả các cặp số Amicable từ 1 đến N. Cặp số Amicable là cặp số mà tổng các ước số của số thứ nhất bằng số thứ hai và ngược lại.
def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total

def find_amicable_pairs(N):
    amicable_pairs = []
    for a in range(1, N + 1):
        b = sum_of_divisors(a)
        if b > a and sum_of_divisors(b) == a:
            amicable_pairs.append((a, b))
    return amicable_pairs

N = int(input("Nhập số N: "))
pairs = find_amicable_pairs(N)

if pairs:
    print("Các cặp số Amicable từ 1 đến", N, "là:")
    for pair in pairs:
        print(pair)
else:
    print("Không có cặp số Amicable nào từ 1 đến", N)