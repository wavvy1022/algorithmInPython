# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게
# 임이 있다.
# 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된
# 다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
# 3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금
# 으로 받게 된다.
# N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램
# 을 작성하시오
# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())

result=0

for i in range(1, n+1):
    arr = list(map(int, input().split()))

    count=0
    diceVal=0
    for j in arr:
        if count<arr.count(j):
            count=arr.count(j)
            diceVal=j

    if count==3:
        a = 10000+(diceVal*1000)
        result = a
    elif count==2:
        b = 1000+(diceVal*100) 
        if result<b:
            result = b
    else:
        c = max(arr)*100
        if result<c:
            result = c  

print(result) 