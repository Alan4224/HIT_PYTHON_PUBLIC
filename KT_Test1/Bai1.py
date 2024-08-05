put = tuple(map(int, input().split()))
lis = []
for i in range(1, len(put)):
    if put[i] == put[i-1]:
        lis.append(put[i])
    else:
        if len(lis) % 5 == 0 and len(lis) % 10 != 0:
            print(put[i])
        lis=[]

