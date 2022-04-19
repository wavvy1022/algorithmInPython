import sys
sys.stdin = open("input.txt","rt")

n, k = map(int, input().split())

#주어진 정수 N의 약수 갯수 카운트 변수 선언
cnt = 0

for i in range(1,n+1):
    if n%i==0:
        # for문을 돌면서 정수 N을 i로 나누었을때 나머지가 없는 약수가 나올 경우 cnt+1
        cnt+=1
    if cnt==k:
        # N의 약수들 중 K번째인 약수가 출력되도록 분기처리
        print(i)
        break
else:
    # 약수의 개수가 K개보다 작을 경우 -1출력
    print(-1)
