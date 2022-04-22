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
import sys
sys.stdin = open("input.txt","rt")

n = int(input())

result=[]

res = 0

for i in range(n):

    # 풀이 1

    # arr = list(map(int, input().split()))

    # count=0
    # diceVal=0

    # for j in arr:
    #     # for문을 수행하면서 한사이클당 반복된 눈의 횟수를 count변수, 중복된 눈의 값을 diceVal에 할당
    #     if count<arr.count(j):
    #         count=arr.count(j)
    #         diceVal=j

    # # 반복된 눈의 횟수에 따른 계산식에 대한 분기처리
    # if count==3:
    #     result.append(10000+(diceVal*1000))
    # elif count==2:
    #     result.append(1000+(diceVal*100))
    # else:
    #     result.append(max(arr)*100)
    
# 모든 결과값(상금값)중 가장 최대값 출력
# print(max(result)) 

    # 풀이 2

    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    #순서에 유의해서 분기처리하기!!
    #만약 2개가 같은 케이스를 먼저 작성할 경우 3개 모두가 같더라도
    #2개가 같은 케이스도 true처리가 되기 때문에 잘못처리될 수 있음!
    if a==b and b==c:
        #주사위 눈 3개 모두 같은 경우
        money = 10000+a*1000
    elif a==b or a==c:
        #주사위 눈 2개가 같은 경우
        money = 1000+(a*100)
    elif b==c:
        money = 1000+(b*100)
    elif a!=b and b!=c:
        #tmp는 sort가된 상태이므로 가장 뒤에있는 값인 c가 큰값이므로 a를 계산해준다.
        money= c*100

    if money>res:
        res=money
print(res)