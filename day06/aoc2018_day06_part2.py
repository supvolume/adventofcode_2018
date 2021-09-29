txt = open("day06_input.txt", "r").read()
#txt = open("day06_test_input.txt", "r").read()
txt_list = txt.split("\n")

# Given max distance
max_distance = 10000
#max_distance = 32 # test distance

# find horizontal and vertical max
x_max = 0
y_max = 0
coor_all = []

for coor in txt_list:
    coor_list = coor.split(", ")
    coor_t = (int(coor_list[0]), int(coor_list[1]))
    coor_all.append(coor_t)
    if int(coor_list[0]) > x_max:
        x_max = int(coor_list[0])
    if int(coor_list[1]) > y_max:
        y_max = int(coor_list[1])

# Calculate Manhattan distance
def manhat_dis(coor1, coor2):
    return abs(coor1[0]-coor2[0]) + abs(coor1[1]-coor2[1])

# Identify the distance to each coor
size = 0

for i in range(x_max+1):
    for j in range(y_max+1):
        grid_coor = (i, j)
        total_dis = 0
        for c in coor_all:
            total_dis += manhat_dis(grid_coor, c)
        if total_dis < max_distance:
            size += 1

print(size)



        
