arr = [int(i) for i in input().split(' ')]

scores_on_top = [0]
for i in arr:
    if i // 3 > scores_on_top[0] // 3:
        scores_on_top.clear()
        scores_on_top.append(i)
    elif i // 3 == scores_on_top[0] // 3:
        scores_on_top.append(i)

n_extra_threes = scores_on_top[0] // 3 - 1
n_ones, n_twos, n_threes = 0, 0, 0
scores_in_mid = []
for i in arr:
    if i == 1:
        n_ones = 1
    elif i == 2:
        n_twos = 1
    elif i // 3 < scores_on_top[0] // 3:
        scores_in_mid.append(i % 3 + 3)

for i,e in enumerate(scores_on_top):   
    scores_on_top[i] = e % 3 + 3

scores_in_mid = set(scores_in_mid)
scores_on_top = set(scores_on_top)

if 3 in scores_on_top and 4 in scores_on_top and 5 in scores_on_top:
    n_ones, n_twos, n_threes = 1, 1, 1
elif 3 in scores_on_top and 4 in scores_on_top:
    n_ones, n_threes = 1, 1
    if 5 in scores_in_mid:
        n_twos = 1
elif 3 in scores_on_top and 5 in scores_on_top:
    n_threes, n_twos = 1, 1
    if 4 in scores_in_mid:
        n_ones = 1
elif 4 in scores_on_top and 5 in scores_on_top:
    n_ones, n_twos, n_threes = 1, 1, 1
elif 3 in scores_on_top:
    if len(scores_in_mid) > 0:
        n_ones, n_twos = 1, 1
    else:
        n_threes = 1
elif 4 in scores_on_top:
    if 5 in scores_in_mid or n_twos == 1:
        n_twos = 2
    else:
        n_ones, n_threes = 1, 1
elif 5 in scores_on_top:
    n_twos, n_threes = 1, 1
    if 4 in scores_in_mid:
        n_ones = 1
else:
    if 4 in scores_in_mid:
        n_ones = 1
    elif 5 in scores_in_mid:
        n_twos = 1

n_threes += n_extra_threes
n_total = n_ones + n_twos + n_threes
print(f'Num of 1s: {n_ones}\nNum of 2s: {n_twos}\nNum of 3s: {n_threes}\n------------\nTotal Num: {n_total}')
