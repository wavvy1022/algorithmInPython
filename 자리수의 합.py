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
    #각 자리수값 배열로 변환
    arr = [int(x) for x in str(num)]
    #배열의 합산처리
    sumNum = sum(arr)
    return sumNum

for x in a:
    #자리수 합산 최대값
    if sumNum<digit_sum(x):
        sumNum = digit_sum(x)
        result = x

print(result)
