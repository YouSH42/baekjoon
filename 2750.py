n = int(input())
P = [input() for _ in range(n)]     #값 입력 받기
int_P = list(map(int, P))           #문자열 int형으로 변형
int_P.sort()
for i in int_P :
    print(i)