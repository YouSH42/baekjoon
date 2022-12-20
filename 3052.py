def remain ( n ) :
    return n % 42

P = [input() for _ in range(10)]    #값 입력 받기
int_P = list(map(int, P))           #문자열 int형으로 변형
re_P = list(map(remain, int_P))

ans = set(re_P)

print(len(ans))