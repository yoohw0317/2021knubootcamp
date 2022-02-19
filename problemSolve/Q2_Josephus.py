# 예시코드 제공 - 강원대학교 컴퓨터정보통신전공 서나o
# 매우 쉬운 문제입니다.
# 이 문제는 실제로 존재하는 '요세푸스 순열'을 다룬 문제이기도 합니다.
# 저는 모듈러 (%)연산을 연습하는데 최적의 문제라고 생각했고, 이 연산은 반복되는 턴제게임에서 실제로 응용됩니다.
# B반과 C반에서 모두 이 문제를 해결한 조가 있었습니다.

tc = int(input())
for i in range(tc):
    n,k = input().split()
    n = int(n)
    k = int(k)-1
    a = list(range(1,n+1))
    num = 0
    name = input().split()
    while len(a)!= 1:
        num = (num+k)%len(a)
        del(a[num])
    print(f'{a[0]} {name[a[0]-1]}')
