data = open('adventday1.txt', 'r')
lines = data.readlines()

answer = 0
prev = 0
num = 0
for i, line in enumerate(lines):
    num = int(line)
    if num > prev:
        answer += 1
    prev = num

print(answer-1)
