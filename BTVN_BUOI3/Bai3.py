# Bài 3: 
# Nhập 2 chuỗi s1, s2 từ bàn phím:
# In ra đảo ngược của chuỗi s1
# Nhập vào 2 số nguyên a, b (1 <=a < b <= len(s2)). In ra chuỗi s2 sau khi đảo ngược chuỗi từ vị trí a đến b.
# In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn
# Trả về chuỗi s4 là đan xen các kí tự của s1 và s2
# VD: s1 = “abc”, s2 = “123” -> s4 = “a1b2c3”
# Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
# VD: s1 = “set”, s2 = “bit” -> “bet” và “sit”

#
s1=input("Nhập chuỗi s1: ")
s2=input("Nhập chuỗi s2: ")
#
s=''.join(reversed(s1))
print(s)
#
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
s=s2[:a]+ ''.join(reversed(s2[a:b+1]))+s2[b-1:]
print(s)
#
x=list(s1)
y=list(s2)
z=[]
m=min(len(x),len(y))
for i in range(m):
    z.append(x[i])
    z.append(y[i])
z.extend(x[m:])
z.extend(y[m:])
r=''.join(z)
print(r)
#
x1=s2[:1]+s1[1:]
x2=s1[:1]+s2[1:]
print(x1)
print(x2)