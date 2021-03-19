# BOJ 10162 전자레인지
time = int(input())

buttons=[300, 60, 10]

count = [0,0,0]

while True:
    if time%10 != 0:
        print(-1)
        break
    else :
        if time==0:
            for i in count:
                print(i, end=' ')
            break
        for i in range(3):
            count[i] = time//buttons[i]
            time = time%buttons[i]

# 다른 정답자
num=int(input())
a=num//300
num=num%300
b=num//60
num=num%60
c=num//10
num=num%10
if c!=0:
    print(-1)
else:
    print("%d %d %d", %(a,b,c))