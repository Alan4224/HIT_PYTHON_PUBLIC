iput=list(input().split(','))
for i in range(len(iput)):
    iput[i]=list(iput[i])
print(iput)
oput=[char for word in iput for char in word]
print(oput)