from audioop import minmax
import sys
# sys.stdin = open("input.txt","rt")

N = int(input())
a = list(map(int, input().split()))

resultVal = 0
resultIdx = 0

#수학점수 평균값 출력
sum = 0
for i in range(len(a)):
    sum += a[i]
#평균점수 반올림처리
avg = round(sum/len(a))

diffValArr = []
for i in range(len(a)):
#평균점수 차이값 절대값으로 변환
    diffValue = abs(a[i]-avg)
    diffValArr.append(diffValue)

#차이값 배열에서 가장 최소값 출력
minValue = min(diffValArr)

minIdxArr = []
#최소값이 단건인지 여러건인지 분기 처리
if diffValArr.count(minValue)>=1:
    for i in range(len(diffValArr)):
        if diffValArr[i] == minValue:
            #여러 최소값index값 배열에 append
            minIdxArr.append(i)
    maxValArr = []
    for i in range(len(minIdxArr)):
        maxValArr.append(a[minIdxArr[i]])
    maxValue = max(maxValArr)
    maxValIdx = a.index(maxValue)
    print(maxValue,maxValIdx+1, sep=' ')
else:
    #단건일 경우 최소값 출력
    minIdx = diffValArr.index(minValue)
    minVal = a[minIdx]
    minValIdx = a.index(minIdx)
    print(minVal,minValIdx+1, sep=' ')






