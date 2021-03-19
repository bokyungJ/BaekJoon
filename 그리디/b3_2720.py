# BOJ 2720 세탁소 사장 동혁

test_case = int(input())

data = []
for i in range(test_case):
    data.append(int(input()))


for money in data:
    q = money//25
    money = money%25
    d = money//10
    money = money%10
    n = money//5
    p = money%5

    print("%d %d %d %d" %(q,d,n,p))
