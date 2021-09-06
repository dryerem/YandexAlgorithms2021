N, i, j = map(int, input().split())
num = i
score1 = 0
score2 = 0
trigger = 0

for num in range(i,N+1):
    if num == j:
        trigger = 1
    if trigger == 0:
        score1 += 1
    elif trigger == 1:
        score2 += 1

for num in range(1,i):
    if num == j:
        trigger = 1
    if trigger == 0:
        score1 += 1
    elif trigger == 1:
        score2 += 1

if score1 > score2:
    print(score2 - 1)
else:
    print (score1 - 1)

