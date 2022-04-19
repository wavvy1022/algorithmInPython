import sys
sys.stdin = open("input.txt","rt")

#케이스 수 입력 input
T= int(input())

#테스크 케이스 수 만큼 for
for i in range(1, T+1):
    #N s e k 및 배열값 입력
    N,s,e,k = map(int, input().split())
    arr = list(map(int, input().split()))
    #각 케이스별 배열에서 s번째부터 e번째까지의 배열 요소 추출
    newArr = arr[s-1:e]
    #추출된 새 배열에서 오름차순 정렬
    newArr.sort()
    #정렬된 새 배열에서 K번째 요소 추출
    answer = newArr[k-1]
    #출력예제 형식에 맞는 값 print
    print("#%d %d" %(t+1,newArr[k-1]))

    

# n, k = map(int, input().split())

