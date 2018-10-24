# O(n^2)
l1 = [8,2,4,9,1,7,5,7,4]

for i, n in enumerate(l1):
    inx, min = i, n
    for j, m in enumerate(l1[(i+1):], start=i+1):
        if m < min:
            inx, min = j, m
    if min != n:
        l1[i], l1[inx] = l1[inx], l1[i]

print(l1)