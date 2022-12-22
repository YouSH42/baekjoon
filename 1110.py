n = int(input())
count = 0
if n < 10:          # 첫 입력 값을 저장한다 만약 한자리 수가 들어왔을경우 0을 추가한다
    n = str(n)
    n = n + '0'

origin_n = int(n)
answer = str(n)

while True :        
    start_n = int(answer[0:1])
    end_n = int(answer[-1])
    endend_n = answer[-1]          #이전의 수 뒷자리 값
    answer = str(start_n + end_n)
    end_n = answer[-1]
    # 기존의 수의 오른쪽 수와 이전에 더한 수의 오른쪽과 더한 값을 저장하고 카운트를 1 올린다
    answer = endend_n + end_n
    #초기값과 현재값이 같으면 반복문 종료
    if int(answer) == origin_n :        
        count += 1
        break
    answer = str(answer)
print(count)