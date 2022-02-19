# 예시코드 제공 - 강원대학교 컴퓨터정보통신전공 서나o
# 사실 제일 어려운 문제였습니다. 하지만 파이썬으로 푼다면 그리 어렵진 않습니다.
# 주석의 설명으로는 표현하기 힘든 감이 있으므로 디버깅해서 직접 코드를 이해해보시는 것을 추천드립니다.
# 해당 풀이가 어렵다면, '(easy)'가 적힌 파일을 참조해주시기 바랍니다.

tc = int(input())

#우선 한자리수인지 확인해야합니다. 한자리수면 반드시 회문수로 취급합니다.
for i in range(tc) :
    n = input()
    if len(n)==1 :
        print("Yes")
        continue
    else : #한자리가 아니면 왼쪽과 오른쪽을 나누어서 확인해봅시다.
        a=int(len(n)/2)
        left = n[:a]
        left = left[::-1]
        right = n[-a:]


    if left == right : #왼쪽과 오른쪽이 같다면 회문수가 맞습니다.
        print("Yes")
        continue
    else : #하지만 아니라면 조금 고통스러운 과정을 거쳐야합니다.
        left = left[::-1]
        mid = n[:-a]+ left[::-1]
        s = str()

    if int(n[-(a+1):]) > int(mid[-(a+1):]) : #수를 절반으로 나누고 둘의 크기를 비교합니다.
        if len(n)%2 ==1 : # 이 조건은 짝수와 홀수를 구분지어줍니다.
            left = str(int(n[:a+1])+1)
            s = left+left[-2::-1]
        else :
            left=str(int(left[:a])+1)
            s=left+left[::-1]
    else :
        if len(n)%2==1 : # 이 조건은 짝수와 홀수를 구분지어줍니다.
            left = str(int(n[:a+1])-1)
            s = left+left[-2::-1]
        else :
            left=str(int(n[:a])-1)
            s=left[:a]+left[::-1]

    if abs(int(n[-(a+1):]) - int(mid[-(a+1):])) >= abs(int(s[-(a+1):]) -int(n[-(a+1):])):
        print(s)
    else :
        print(mid)
