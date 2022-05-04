import sys
import numpy as np
sys.stdin = open("input.txt","rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
a2 = [list(map(int, input().split())) for _ in range(m)]

# 모래시계 영역 총합 변수
res = 0

# 탐색 영역 포인터
s = 0
e = n

for i in range(0,len(a)):
    # 배열 회전 수정 시작
    for j in a2:
        # a2배열리스트에 첫번째 요소 추출 후 회전을 수행할 행 가져오기
        if i+1== j[0]:
            # 이동 값
            moveVal = j[2]
            # 이동 방향 분기처리(0=>왼쪽, 1=>오른쪽)
            newArr = []
            if(j[1]==0):
                # 왼쪽일 경우 moveVal에서 음수방향으로
                newArr = np.roll(a[i],-moveVal)
                a[i].clear()
                a[i].extend(newArr)
            else:
                newArr = np.roll(a[i], moveVal)
                a[i].clear()
                a[i].extend(newArr)
    # 배열 회전 수정 완료

    # 모래시계 모양 영역 값 추출 시작
    # for문 돌면서 res에 탐색영역 총합계산 후 포인터 처리
    for k in range(s, e):
        res += a[i][k]
    #2차원 배열 중간지점 분기처리
    if (n//2)>i:
        # 2차원배열 중간지점 이전에는 e,s 포인터 사이 간격 감소 처리
        s+=1
        e-=1
    else:
        # 중간지점 이후 e,s포인터 사이 간경 증가 처리
        s-=1
        e+=1
print(res)