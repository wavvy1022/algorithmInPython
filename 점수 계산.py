# OX 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말한다. 여러 개의 OX 문제로 만들어진
# 시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해서 다음과 같이 점수 계산을 하기
# 로 하였다. 1번 문제가 맞는 경우에는 1점으로 계산한다. 앞의 문제에 대해서는 답을 틀리다가
# 답이 맞는 처음 문제는 1점으로 계산한다. 또한, 연속으로 문제의 답이 맞는 경우에서 두 번째
# 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로 계
# 산한다.
# 예를 들어, 아래와 같이 10 개의 OX 문제에서 답이 맞은 문제의 경우에는 1로 표시하고, 틀린 경
# 우에는 0으로 표시하였을 때, 점수 계산은 아래 표와 같이 계산되어, 총 점수는
# 1+1+2+3+1+2=10 점이다.
# 시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램을 작성하시오. 

import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(input().split())

strArr = "".join(a)
#문자로 입력된 값에서 0값을 기준으로 split
splitArr = strArr.split("0")

result = 0

def arrAdd(arr):
    cnt=0
    sum=0
    # 연속된 정답의 경우 cnt값을 증가시키면서 점수 계산
    for i in arr:
        cnt +=1
        sum += cnt
    return sum

for i in splitArr:
    arr = []
    if i !='':
        # 0을 기준으로 자른 값 중에 빈문자열이 아닌 요소를 list로 변환후 합산 계산 function으로 전달
        sum = arrAdd(list(i))
        # 각각의 배열에 대한 sum값을 총점변수에 더함
        result += sum

print(result)