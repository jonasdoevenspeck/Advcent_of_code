
# %% Day 2 Part 1
a_file = open("AoC_2_input.txt", "r")
dirs = [line.strip() for line in a_file]

hor = 0
depth = 0

for dir in dirs:
    move, mag = dir.split()
    mag = int(mag)
    if move == 'forward':
        hor += mag
    elif move == 'down':
        depth += mag
    elif move == 'up':
        depth -= mag

print(hor*depth)

# %% Day 2 Part 2
hor = 0
depth = 0
aim = 0

for dir in dirs:
    move, mag = dir.split()
    mag = int(mag)
    if move == 'forward':
        hor += mag
        depth += aim*mag
    elif move == 'down':
        #depth += mag
        aim += mag
    elif move == 'up':
        #depth -= mag
        aim -= mag

print(hor*depth)

# %%
