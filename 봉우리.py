import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 2차원 배열 a의 상,하 0으로 초기화
a.insert(0, [0]*n)
a.append([0]*n)

# 2차원 배열 a의 좌,우 0으로 초기화
for i in range(0,len(a)):
    a[i].insert(0,0)
    a[i].append(0)

# 봉우리 개수 변수
cnt = 0

# x축 y축   
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 0으로 초기화 된 영역을 제외한 2차원 배열 2중 for문
for i in range(1,n+1):
    for j in range(1,n+1):
        # python all()함수=> 함수안에 조건이 모두 참일때만 true로 반환
        # 상하좌우 4방향 탐색
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)