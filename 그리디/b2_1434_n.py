# BOJ 1434 책 정리

# 이거 그냥 박스 용량에서 책의 크기 빼면 되는데 코테적으로 풀어본당

# 박스의수, 책의 수
n, m = map(int, input().split())
# 박스의 용량
box_size = list(map(int, input().split()))
# 책의 용량
book_size = list(map(int, input().split()))

i = 0 
while True:
    if box_size[i]>book_size[i]:
        box_size[i]-=book_size[i]
    else :
        
# 안할랭