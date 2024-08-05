n = int(input())
hungDict = {}
for i in range(n):
    key, value = input().split()
    hungDict[key] = value
out=set(hungDict.values())
out=list(out)
print(hungDict.get(out[-2]))
