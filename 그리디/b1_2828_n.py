# BOJ 2828 사과 담기 게임

# 스크린 너비, 바구니 너비
n, m = map(int, input().split())
# 사과 수
a = int(input())

count = 0
for i in range(a):
    f = int(input())
    d = f-