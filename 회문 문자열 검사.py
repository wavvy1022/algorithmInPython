import sys
sys.stdin = open("input.txt","rt")

n = int(input())

for T in range(n):
    
    #대소문자 구분이 없으므로 입력값 받을때 모두 소문자로 변환
    text = input().lower()

    # 입력받은 텍스트 배열로 변환
    strArr = list(text)
    
    # # 배열 텍스트 reverse처리
    # reverseArr = reversed(strArr)
    # # reverse처리된 배열 text로 변환
    # reverseTxt = ''.join(reverseArr)

    # 내장함수 안쓰는 ver

    reverseArr = []
    # for문 역순으로 수행해서 reverse
    for i in range(len(strArr)-1,-1,-1):
        reverseArr.append(strArr[i])
    
    reverseTxt = ''.join(reverseArr)

    # 케이스별 회문문자 여부 출력

    if text==reverseTxt:
        print("#%d %s" %(T+1,"YES"))
    else:
        print("#%d %s" %(T+1,"NO"))