A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if B >= C :         #B가 C보다 크면 손익분기점이 X -1로 출력
    print(-1)
else:
    print(A//(C-B) + 1)