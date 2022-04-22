import sys
sys.stdin = open("input.txt","rt")

n = int(input())

for i in range(n):
    
    #대소문자 구분이 없으므로 입력값 받을때 모두 소문자로 변환
    text = input().lower()

    # 입력받은 텍스트 배열로 변환
    strArr = list(text)
    
    # 배열 텍스트 reverse처리
    reverseArr = reversed(strArr)
    # reverse처리된 배열 text로 변환
    reverseTxt = ''.join(reverseArr)
    
    # 케이스별 회문문자 여부 출력
    if text==reverseTxt:
        print("#%d %s" %(i+1,"YES"))
    else:
        print("#%d %s" %(i+1,"NO"))