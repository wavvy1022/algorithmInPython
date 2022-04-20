from audioop import minmax
import sys
# sys.stdin = open("input.txt","rt")

N = int(input())
a = list(map(int, input().split()))

resultVal = 0
resultIdx = 0

#수학점수 평균값 출력및 반올림처리
avg = round(sum(a)/len(a))
# float("inf") 양의 무한대(최대값으로 설정)
min = float("inf")
for idx, x in enumerate(a):
#enumerate : 배열 각각요소의 값과 index값을 쌍으로 대응해 주는 함수
    tmp=abs(x-avg)
    if(tmp<min):
        min = tmp
        score = x
        res = idx+1
    #elif => else if
    elif tmp==min:
        if x>score:
            #평균차가 동일한 경우 점수가 높은 케이스의 경우에만 답으로 설정
            score=x
            res=idx+1
print(avg,res, sep=' ')