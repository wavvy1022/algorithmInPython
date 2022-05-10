from re import S
import sys
sys.stdin = open("input.txt","rt")

a = [list(map(int, input().split())) for _ in range(9)]


# 배열 중복 체크 함수
def check(a):
    for i in range(len(a)):
        # ch1=> 행 중복체크 배열
        # ch2=> 열 중복체크 배열
        ch1=[0]*10
        ch2=[0]*10
        for j in range(len(a)):
            # 1~9까지의 수가 중복이 없어야 하므로 1~9까지의 인덱스가 있는
            # ch(check)배열을 생성 후 각 요소의 값을 인덱스로하여 1로 초기화 후 
            # 1~9까지의 값이 모두 있을 경우 ch배열의 총합이 9
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        #총합이 9가 아닐 경우 중복된 값이 있으므로 "no" 출력 후 break 
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    return True

if check(a):
    print("YES")
else:
    print("NO")