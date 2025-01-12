x = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    x.append([score, name])
x.sort()
minimum_score = x[0][0]
while x != [] and x[0][0] == minimum_score:
    x.pop(0)
if x != []:
    second_minimum_score = x[0][0]
    for b in x:
        if b[0] == second_minimum_score:
            print(b[1])
