import sys
# sys.stdin = open("input.txt","rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
#set자료구조는 중복된 요소는 제거된 상태로 append
res = set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1, n):
            #중복 제거된 상태의 값으로 저장
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])


