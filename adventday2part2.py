with open('adventday2.txt') as f:
    lines= f.read().splitlines() 

# data = open('adventday2.txt', 'r')
# lines = data.readlines()
# lines = [i.split for i in lines]

forward = 0
depth = 0
aim = 0

for line in lines:
    if line.split()[0] == "forward":
        forward += (int)(line.split()[1])
        depth += (int)(line.split()[1]) * aim
    elif line.split()[0] == "up":
        aim -= (int)(line.split()[1])
    elif line.split()[0] == "down":
        aim += (int)(line.split()[1])

print(depth * forward)
