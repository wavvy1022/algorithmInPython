# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
# 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
# 꼭 작성해서 프로그래밍 하세요.

import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))

sumNum = 0
result = 0

#자리수 합산 function
def digit_sum(num):
    # #각 자리수값 배열로 변환
    # arr = [int(x) for x in str(num)]
    # #배열의 합산처리
    # sumNum = sum(arr)
    # return sumNum

    # 다른 풀이
    sum = 0
    while num>0:
        # 10으로 나누었을때의 나머지값을 sum변수에 더함
        sum+=num%10
        # 10으로 나눴을때의 몫값을 num변수에 할당
        # 나머지가 1자리수까지 반복 => 각각 자리수에 대한 합산처리
        num=num//10
    return sum

for x in a:
    #자리수 합산 최대값
    if sumNum<digit_sum(x):
        sumNum = digit_sum(x)
        result = x

print(result)
