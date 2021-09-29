txt = open("day06_input.txt", "r").read()
#txt = open("day06_test_input.txt", "r").read()
txt_list = txt.split("\n")

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


# Identify the closest coor in each grid
grid = []
edge = []
for i in range(x_max+1):
    for j in range(y_max+1):
        grid_coor = (i, j)
        closest = x_max+y_max
        coor_closest = ""
        for c in coor_all:
            m_dis = manhat_dis(grid_coor, c)
            if m_dis == closest:
                coor_closest = 0
            elif m_dis < closest:
                closest = m_dis
                coor_closest = c
        grid.append(coor_closest)

        # Find the coor that locate at the edge
        if i == 0 or j == 0 or i == x_max or j == y_max:
            edge.append(coor_closest)

edge = list(set(edge))

# Count
coor_dict = {}
for i in grid:
    if i not in edge:
        if i in coor_dict:
            coor_dict[i] += 1
        else:
            coor_dict[i] = 1

# print max
coor_dict = dict(sorted(coor_dict.items(), key=lambda item: item[1], reverse=True))
print(list(coor_dict.values())[0])
