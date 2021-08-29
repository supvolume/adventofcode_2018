txt = open("day03_input.txt", "r").read()
#txt = open("day03_test_input.txt", "r").read()
txt_list = txt.split("\n")

# Func that return coordination list
def get_coor(order):
    coor_list = []
    order_list = order.split(" ")

    start_coor = order_list[2].split(",")
    start_x = int(start_coor[0])
    start_y = int(start_coor[1][:-1])

    rec_size = order_list[3].split("x")
    width_x = int(rec_size[0])
    height_y = int(rec_size[1])

    # Create coordination
    for i in range(start_x, start_x + width_x):
        for j in range(start_y, start_y + height_y):
            coor_list.append(str(i)+","+str(j))
    return coor_list
    

# Record the rectangle coordination and the amount that it gets requested
coor_dict = dict()
overlap = set()

for order in txt_list:
    coor_list = get_coor(order)
    for i in coor_list:
        if i in coor_dict:
            coor_dict[i] += 1
            overlap.add(order)
        else:
            coor_dict[i] = 1


# Part 1 answer
count = 0
for i in list(coor_dict.values()):
    if i != 1:
        count += 1
print(count)

# Part 2 answer
# Reverse the order list to find duplicate patterns
coor_dict_re = dict()
for order in reversed(txt_list):
    coor_list = get_coor(order)
    for i in coor_list:
        if i in coor_dict_re:
            coor_dict_re[i] += 1
            overlap.add(order)
        else:
            coor_dict_re[i] = 1
            
print(set(txt_list) - overlap)
