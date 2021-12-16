with open('adventday2.txt') as f:
    lines= f.read().splitlines() 

# data = open('adventday2.txt', 'r')
# lines = data.readlines()
# lines = [i.split for i in lines]

forward = 0
depth = 0

for line in lines:
    if line.split()[0] == "forward":
        forward += (int)(line.split()[1])
    elif line.split()[0] == "up":
        depth -= (int)(line.split()[1])
    elif line.split()[0] == "down":
        depth += (int)(line.split()[1])

print(depth * forward)
