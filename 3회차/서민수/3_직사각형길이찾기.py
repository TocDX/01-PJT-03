import sys
# a,b,c가 있을때 1 2 1로 입력받으면
# 나머지 숫자는 2로 된다 만약 세 숫자가 같으면 나머지 숫자도 같게 된다
# 그렇다면 사용할 수 있는건 조건문이라고 생각한다.
# a와 b가 같지 않다면 d와 c는 a와b랑 무조건 붙어있으니
# a+b-c하면 d가 나온다고 생각한다
# 나오는 값을 리스트에 저장한다

sys.stdin = open("_직사각형길이찾기.txt")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    a, b, c, = map(int,input().split())
    lst = [a,b,c]

    if a != b:
        d = a+b-c
    else:
        d = c
        lst.append(d)
    print("#{} {}".format(test_case,d))
