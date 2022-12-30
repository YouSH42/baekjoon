def chage_up(u):
    return u.upper()
dic = {}
count = 0
num_list = list(input())
up_chage = list(map(chage_up, num_list))
up_chage.sort()

past = up_chage[0]
for i in up_chage :
    if past == i :
        count += 1
        dic[past] = count
    elif past != i :
        dic[past] = count
        count = 1
        past = i

for i in dic :
    maxVal = dic[i]
    if maxVal < dic[i] :
        maxVal = dic[i]
    elif maxVal > dic[i] :
        continue
    else :
        break
print(maxVal)