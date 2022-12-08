def list_chunk(lst, n):     #리스트 분할
    return [lst[i:i+n] for i in range(0, len(lst), n)]

count = int(input())        #테스트 케이스 개수
P = [input() for _ in range(count)]  #여러줄 입력 받기
score = 0 ; plus = 0 ; tmp = 'X' ; answer = []     #변수 선언
for i in range(count) :
    list_div = list_chunk(P[i],1)   #리스트 안의 문자열 한 글자씩 분할
    for j in list_div :
        if j == 'O' :
            if tmp == 'O' :
                score =  score + plus + 1
            elif tmp == 'X' :
                score += 1
            tmp = j     #이전의 OX결과값 저장
            plus += 1   #추가점수
        elif j == 'X' :
            tmp = j
            plus = 0    #추가점수 초기화
    answer.append(score)
    score = 0 ; plus = 0 ; tmp = 'X'    #변수 초기화
for k in answer :
    print(k)