# 예시코드 제공 - 강원대학교 컴퓨터정보통신전공 서나o
# 가장 배점이 적지만 실제로는 5문제중 2~3번째로 어려울 수도 있는 문제입니다.
# 저는 이 문제를 list 및 set 자료구조를 연습하기 위해 출제했습니다.
# 하지만 B반에서 set 자료구조를 다루지 않아서 list 형식으로 우선 해답코드를 제시합니다.
# 이 문제는 2차원 리스트를 구현해서, 서로 연결되어 있는 지역을 묶을 수 있으면 쉽게 판별할 수 있습니다.
# 만약 A B C D지역이 서로 연결되어있고 F G H가 떨어져있다면, [[A, B, C, D], [F, G, H]]로 구현 가능하겠죠?
# 많은 분들이 이 문제를 도전해주셨지만 아쉽게도 제출하신 조는 없었습니다.

n,k=input().split()
n = int(n)-1
k = int(k)
a = [input().split()]
for i in range(n) :
    x,y = input().split()
    num = -1
    for j in range(len(a)) :
        if x in a[j] :
            if num >= 0 :
                a[num].extend(a[j])
            else :
                a[j].append(y)
                num = j
        elif y in a[j] :
            if num >= 0 :
                a[num].extend(a[j])
            else :
                a[j].append(x)
                num = j
        elif j == len(a)-1 and num == -1 :
            a.append(list(x))
            a[a.index(list(x))].append(y)
for i in range(k) :
    x,y = input().split()
    for j in range(len(a)) :
        if x in a[j] and y in a[j] :
            print("도달가능")
            break;
        elif j == len(a)-1 :
            print("에덴동산")
