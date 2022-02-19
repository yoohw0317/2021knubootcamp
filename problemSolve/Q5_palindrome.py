# 코드 출처: 부트캠프 B반 코담 - 박수o, 이정o
# 사실 실행시간 제한을 걸지 않았을 때 이렇게 푸는 사람이 나오지 않을까 생각은 했지만 정말 나올줄은 몰랐습니다.
# 시간이 넉넉하게 많다면 이렇게 직접 찾아보는 것도 나쁘지 않은 방법이죠?
# 굳이 어렵다는 생각의 틀에 갇히지 않고 직접 시도해본 멋진 사레입니다.
# 이 답안지를 보고 검수했던 사람들 모두 좋아했습니다, 저도 엄청 웃었구요.

def test(n):
    x = n
    y = n
    while True:
        if str(y) == str(y)[::-1]:
            return y
        y += 1
        if str(x) == str(x)[::-1]:
            return x
        x -=  1
    return int(bin(n)[::-1][:-2], 2)

n = int(input())
if test(n) == n:
     print("yes")
else :
     print(test(n));
