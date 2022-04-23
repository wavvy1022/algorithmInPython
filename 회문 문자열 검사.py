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

    # reverseArr = []
    # # for문 역순으로 수행해서 reverse
    # for i in range(len(strArr)-1,-1,-1):
    #     reverseArr.append(strArr[i])
    
    # reverseTxt = ''.join(reverseArr)

    #다른 풀이3
    size = len(text)
    # 문자열을 반으로 나눠서 나눈값을 기준으로 대칭된 텍스트가 같은지 체크 후
    # 하나라도 다른 텍스트가 나올 경우 for문 break
    for i in range(size//2):
        if text[i]!=text[-1-i]:
            print("#%d NO" %(T+1))
            break
    else:
        print("#%d YES" %(T+1))

    # 케이스별 회문문자 여부 출력

    # if text==reverseTxt:
    #     print("#%d %s" %(T+1,"YES"))
    # else:
    #     print("#%d %s" %(T+1,"NO"))