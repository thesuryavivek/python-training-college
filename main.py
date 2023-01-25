n = int(input())
arr = list(map(int, input().split(' ')))

result = []

for i in arr:
    if arr.count(i) > 1 and i not in result:
        result.append(i)

if len(result) < 1:
    print('No elements found')
else:
    print(' '.join(list(map(str, result))))