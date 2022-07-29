import sys

sys.stdin = open("_소득불균형.txt")

# 평균 소득의 이하인 사람을 골라내라
# 사람수 소득의 양을 받아야 한다
# 조건문이 필요 해보인다 총 소득을 사람 수대로 나뉘어
# 나온 평균 소득의 값이 개인 소득의 양을 비교하여 
# 개인의 소득 N이 평균 소득의 값보다 작거나 같을 때 
# 사람들의 수를 세어줘라.

# 필요한건 사람의 수와 소득의 양을 받을 input()함수
# 소득의 양은 split으로 쪼개서 받아야 할 것 같다 숫자가 여러개로 나누어지니
# 또 처음부터 끝까지 순회를 해야 하니 for문을 사용해야 할 것 같다.
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for A in range(1, T + 1):
    H = int(input())
    N = list(map(int,input().split()))
    avg = sum(N)/H
    cnt = 0 
    for i in N:
        if i <= avg:
            cnt+=1
    print("#{} {}".format(A,cnt))

