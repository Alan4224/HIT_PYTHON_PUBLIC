put = tuple(map(int, input().split()))
lis = []
for i in range(2, len(put)):
    if put[i] != put[i-1]:
        if put.count(put[i]) % 5 == 0 and  put.count(put[i])% 10 != 0:
            lis.append(put[i])
print(lis)

