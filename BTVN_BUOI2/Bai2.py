# Bài 2:  Cho 2 số a, b bất kỳ. Hãy in ra màn hình:
# a.    a cộng b
# b.    a trừ b
# c.    a nhân b
# d.    a chia lấy nguyên b
# e.    a mũ b
# f.     a chia dư b
# g.    so sánh a và b (lớn hơn, nhỏ hơn hay bằng)
# h.    a AND b
# i.     a OR b
# j.     a XOR b
# k.   NOT a == b
# l.    a dịch phải 1 đơn vị
# m.  a dịch trái 1 đơn vị

a = 10
b = 5
print ('{} cộng {} bằng {}'.format(a, b, a + b))
print(f'{a} trừ {b} bằng {a - b}')
print(a,'nhân',b,'bằng',a*b)
print(a,'chia',b,'bằng',a//b)
print(a,'mũ',b,'bằng',a**b)
print(a,'chia',b,'dư',a%b)
if a>b:
    print(a,'lớn hơn',b)
elif a==b:
    print(a,'bằng',b)
else:
    print(a,'bé hơn',b)
print(a and b)
print(a or b)
print(a ^ b)
print(not a == b)
print(a >> 1)
print(a << 1)