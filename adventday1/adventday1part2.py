data = open('adventday1.txt', 'r')
lines = data.readlines()
lines = [int(i) for i in lines]

answer = 0
currentWindow = 0
prevWindow = 0

i = 2
for line in lines[2:]:
    currentWindow = line + lines[i-1] + lines[i-2]
    if currentWindow > prevWindow:
        answer += 1
    prevWindow = currentWindow
    i += 1

print(answer-1)
