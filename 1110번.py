def list_chunk(lst, n):     #리스트 분할
    return [lst[i:i+n] for i in range(0, len(lst), n)]

count = int(input())        #테스트 케이스 개수
P = [input() for _ in range(count)]  #여러줄 입력 받기

for i in range(count) :
    a = list_chunk(P[i],1)
    print(a)