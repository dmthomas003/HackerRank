n = int(raw_input())
arr = map(int, raw_input().split())


for i in arr:
    print i, arr.index(i)

"""
for i in arr:
    if arr.index(i) == n:
        print i
    elif i > arr[arr.index(i)+1]:
        print i


"""
