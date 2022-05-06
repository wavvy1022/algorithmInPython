import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)

for i in range(0,len(a)):
    a[i].insert(0,0)
    a[i].append(0)

cnt = 0
for i in range(1,len(a)-1):
    
    for j in range(1,n+1):
        arr = []
        arr.append(a[i-1][j])
        arr.append(a[i+1][j])
        arr.append(a[i][j-1])
        arr.append(a[i][j+1])
        arr.append(a[i][j])
        if max(arr)==a[i][j]:
            cnt += 1
print(cnt)