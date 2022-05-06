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

# 0으로 초기화 된 영역을 제외한 2차원 배열 2중 for문
for i in range(1,n+1):
    for j in range(1,n+1):
        # 요소의 상,하,좌,우 영역 배열에 append후 해당 요소가 배열에서 최대값일 경우
        # cnt +1처리
        arr = []
        arr.append(a[i-1][j])
        arr.append(a[i+1][j])
        arr.append(a[i][j-1])
        arr.append(a[i][j+1])
        # arr최대값과 봉우리 판별요소 비교해서 arr최대값보다 클 경우 카운트 추가(같은case 제외!)
        if max(arr)<a[i][j]:
            cnt += 1
print(cnt)