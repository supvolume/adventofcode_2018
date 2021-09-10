txt = open("day04_input.txt", "r").read()
#txt = open("day04_test_input.txt", "r").read()
txt_list = txt.split("\n")

txt_list = sorted(txt_list)

# Find the minute that each guard asleep
all_guard = []
each_guard = {}
min_asleep = []
time_fall = 0
time_wake = 0

for record in txt_list:
    detail = record.split(" ")
    if detail[2] == "Guard":
        if len(each_guard) > 0:
            all_guard.append(each_guard)
        each_guard = {}
        min_asleep = []
        each_guard["id"] = detail[3]
        each_guard["begin"] = detail[1][3:5]
    elif detail[2] == "falls":
        time_fall = int(detail[1][3:5])
    elif detail[2] == "wakes":
        time_wake = int(detail[1][3:5])
        for i in range(time_fall, time_wake):
            min_asleep.append(i)
    each_guard["min_asleep"] = min_asleep
    
all_guard.append(each_guard)

# Merge duplicate guard ID
uniq_guard = {}

for guard in all_guard:
    if guard["id"] in uniq_guard:
        uniq_guard[guard["id"]] += guard["min_asleep"]
    else:
        uniq_guard[guard["id"]] = guard["min_asleep"]

# Part 1
# Print the id that have the most asleep time
top = 0
top_id = ""
for k, v in uniq_guard.items():
    if len(v) > top:
        top = len(v)
        top_id = k
print(top_id)

# Find the minute that guard asleep the most
min_count = {}
for i in uniq_guard[top_id]:
    if i in min_count:
        min_count[i] += 1
    else:
        min_count[i] = 1
min_count = dict(sorted(min_count.items(), key=lambda item: item[1], reverse=True))
print(min_count)

# Part 2
top_min = 0
top_min_count = 0
top_min_id = ""
for k, v in uniq_guard.items():
    min_count2 = {}
    for i in v:
        if i in min_count2:
            min_count2[i] += 1
        else:
            min_count2[i] = 1
    min_count2 = dict(sorted(min_count2.items(), key=lambda item: item[1], reverse=True))
    if len(min_count2) > 0:
        id_top_min = list(min_count2.keys())[0]
        id_top_count = list(min_count2.values())[0]
        if id_top_count > top_min_count:
            top_min = id_top_min
            top_min_id = k
            top_min_count = id_top_count

print(top_min_id, top_min)

