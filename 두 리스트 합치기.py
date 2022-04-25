# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 리스트 합치기
# sumArr = a+b
# sumArr.sort()

# a,b리스트는 이미 정렬이 된 상태로 입력이 되기 때문에
# 상단과 같이 단순히 리스트를 합친상태에서 다시 sort를 돌리는것은
# 시간복잡도상 좋지 않은 방법!

# 포인터
p1=p2=0

# 결과 리스트
c=[]

# 둘중의 하나의 포인터가 끝날때 까지
# =>하나의 포인터가 끝나면 남은 포인터의 배열 요소는 이미sort가 된 상태기 때문에
# 그대로 결과 리스트에 append하면 되기 때문
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1<n:
    arr = a[p1:len(a)]
    c.extend(arr)
else:
    arr = b[p2:len(b)]
    c.extend(arr)

for i in c:
    print(i, end=" ")