with open('./in/25.txt') as f:
    lines = f.read().strip().splitlines()

def parse_snafu(snafu):
    num = 0
    for digit in snafu:
        num *= 5
        if digit == '-':
            num -= 1
        elif digit == '=':
            num -= 2
        else:
            num += int(digit)
    return num

def to_snafu(num):
    digits = []
    while num:
        m = num % 5
        if m == 3:
            digits.append('=')
            num += 2
        elif m == 4:
            digits.append('-')
            num += 1
        else:
            digits.append(str(m))
            num -= m
        num //= 5
    return ''.join(reversed(digits))

nums = [parse_snafu(line) for line in lines]
k = sum(nums)

ans = to_snafu(k)
print(ans)

checksum = parse_snafu(ans)
assert k == checksum, (k, checksum)
