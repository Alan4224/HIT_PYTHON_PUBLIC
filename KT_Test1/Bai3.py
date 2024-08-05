n = int(input())
hungDict = {}
for i in range(n):
    key, value = input().split()
    hungDict[key] = value
out=set(hungDict.values())
out=list(out)
find = out[-2]
for key, value in hungDict.items():
    if value == find:
        print(key)

