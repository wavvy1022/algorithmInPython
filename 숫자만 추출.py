import sys
import re
sys.stdin = open("input.txt","rt")

t= input()

# 숫자 정규표현식
regex = re.compile('\d')
regex.search

numArr = []

for i in t:
    # 정규표현식으로 입력된 텍스트에서 숫자인 요소들만 추출
    if regex.search(i) is not None:
        numArr.append(i)

# 숫자인 요소들만 추출된 배열을 문자열로 변환후 다시 int로 변환시킴으로서
# 앞자리의 0은 자연수화 하면서 삭제처리 되도록함
num = int("".join(numArr))
print(num)

cnt=0
for i in range(1,num+1):
    if num%i==0:
        cnt+=1

print(cnt)