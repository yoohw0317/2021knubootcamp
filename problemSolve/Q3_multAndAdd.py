# 예시코드 제공 - 강원대학교 컴퓨터정보통신전공 서나o
# 쉬운 문제중 하나입니다.
# 문자열을 자유자재로 나눌 수 있으면 풀 수 있습니다.
# split을 이용해서 우아하게 풀 수도 있지만 이런 방법으로도 풀 수 있습니다.
# 그리고 우선적으로 *을 처리하고 +을 처리하면 정확한 계산 결과를 유도할 수 있습니다.
# 실제로 이 문제는 B반에서 정답으로 제출한 조가 있었습니다.

tc = int(input())
for tc in range(tc):
    s = input()
    a = []
    n = 0
    result = ""

    for i in range(len(s)):
        if s[i] == '+' or s[i] == '*':
            a.append(s[n:i])
            a.append(s[i])
            n = i + 1
    a.append(s[n:s.find('=')])

    while '*' in a:
        n = a.index('*')
        a[n - 1] = str(int(a[n - 1]) * int(a[n + 1]))
        del a[n]
        del a[n]

    while '+' in a:
        n = a.index('+')
        a[n - 1] = str(int(a[n - 1]) + int(a[n + 1]))
        del a[n]
        del a[n]

    result = (str)(s[s.find('=') + 1:] == a[0])
    if result == "False":
        result += " " + a[0]
    print(result)
