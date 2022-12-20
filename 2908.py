a, b = input().split()
re_a = int(a[::-1])
re_b = int(b[::-1])

if re_a > re_b :
    answer = re_a
else :
    answer = re_b
    
print(answer)