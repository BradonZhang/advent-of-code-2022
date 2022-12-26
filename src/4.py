with open('./in/4.txt') as f:
    lines = f.read().strip().splitlines()

total1 = 0
total2 = 0
for line in lines:
    ax, ay, bx, by = map(int, line.replace(',', '-').split('-'))
    total1 += bx <= ax <= ay <= by or ax <= bx <= by <= ay
    total2 += ax <= bx <= ay or bx <= ax <= by

print(total1)
print(total2)
