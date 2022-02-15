
# %% Day 1 Part 1
a_file = open("AoC_1_input.txt", "r")
depths = [int(line.strip()) for line in a_file]

incr_cnt = 0
for depth_idx in range(1,len(depths)):
    if depths[depth_idx]>depths[depth_idx-1]:
        incr_cnt +=1
print(incr_cnt)

# %% Day 1 Part 2
incr_cnt = 0
for depth_idx in range(1,len(depths)-2):
    sum_1 = depths[depth_idx-1]+depths[depth_idx]+depths[depth_idx+1]
    sum_2 = depths[depth_idx]+depths[depth_idx+1]+depths[depth_idx+2]
    if sum_2>sum_1:
        incr_cnt +=1
print(incr_cnt)
 
# %% Day 2 Part 1


