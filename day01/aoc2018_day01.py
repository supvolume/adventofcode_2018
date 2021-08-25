txt = open("day01_input.txt", 'r').read()
txt_list = txt.split("\n")
int_list = list(map(int, txt_list))

# Part 1 answer
print(sum(int_list))

# Part 2
freq_sum = 0
result_list = []
found = False
while found == False:
    for i in int_list:
        freq_sum += i
        if freq_sum not in result_list:
            result_list.append(freq_sum)
        else:
            print(freq_sum)
            found = True
            break
