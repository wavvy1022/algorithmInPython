import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 초기화는 최소값으로(음의 무한대)
largest = float("-inf")

for i in range(n):
    # 행의 합과 열의 합 변수를 따로 지정
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

sum1=sum2=0

# 대각선의 합을 구하는 변수
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
print(largest)