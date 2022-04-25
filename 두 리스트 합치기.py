# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

sumArr = a+b
sumArr.sort()
print(sumArr)