import sys

sys.stdin = open("_문자열의거울상.txt")
# 문제를 보면 떠오는건 reverse 혹은 역순?
# 또는 슬라이싱으로..?
# 또는 규칙을 찾아내는 것?
# 규칙이 있다면 어떤것일까
# qqqqpppbbd, bddqqqpppp
# q와p d와b가 바뀌는게 아닐까하고 생각하면
# q부터 시작하는게 아니라 d부터 시작 해서 
# dbbpppqqqq 이지 않을까 생각한다
# 역순을 해서 바꾼것 같다


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word =input()
    for i in word: