# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다. 

import sys
sys.stdin = open("input.txt","rt")

n = int(input())

ch=[0]*(n+1)
cnt=0

for i in range(2, n+1):
    if ch[i]==0:
        cnt +=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)