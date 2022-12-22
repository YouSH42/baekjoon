def fake(sub):              #새로운 평균
    return sub/max_n*100

fk_total = 0
n = int(input())
subs = list(map(int, input().split()))
max_n = max(subs)               #리스트 값 중 최대 값 찾기
fk_subs = list(map(fake,subs))
for i in fk_subs:
    fk_total += i

print(fk_total/n)