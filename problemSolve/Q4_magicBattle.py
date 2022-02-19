# 예시코드 제공 - 강원대학교 컴퓨터정보통신전공 서나o
# 여러가지 방식으로 풀 수 있는 문제입니다.
# 우선 이 문제를 낸 의도는 여러가지 부울 대수를 다루면서 프로그램의 상태를 조정하도록 냈습니다.
# 하지만 이 코드의 경우 부울대수가 아닌 stamina 라는 변수를 이용해서 프로그램의 상태를 결정합니다.
# 어쩔티비 주문의 경우 자신의 주문을 지우지 않기 때문에 조금 더 생각을 해보아야 합니다.
# 주문의 조건을 잘 구현한다는 것이 꽤나 어려우셨을 문제입니다.

tc = int(input())
for tc in range(tc) :
    a = input().split()
    if(len(a) > 8) :
        del a[8:]
    a.reverse()
    stamina = 0
    i=3
    mana = True
    while len(a) != 0 :
        if stamina < -1 :
            print("곰두리 사망")
            break
        if a[0] == "무자비" :
           if len(a)<4 :
                i = len(a)-1
           for k in range(i) :
                del a[1]
        elif a[0] == "곰돌다운" :
            stamina -= 1
        elif a[0] == "종강이야" :
            stamina += 1
        elif a[0] == "어쩔티비" :
            if len(a)>1 and (a[1] == "무자비" or a[1] == "곰돌다운") :
                del a[1]
        else :
            print("마법역류")
            mana = False
        del a[0]
    if mana :
        if stamina >= 0 :
            print("곰두리 생존")
        else :
            print("곰두리 사망")
