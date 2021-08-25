txt = open("day02_input.txt", 'r').read()
txt_list = txt.split("\n")

# Test list
test_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

# Part 1
twice_count = 0
three_count = 0
twice_found = False
three_found = False

for box_id in txt_list:
    box_dict = dict()

    # Count each letter in box id 
    for letter in box_id:
        if letter in box_dict:
            box_dict[letter] += 1
        else:
            box_dict[letter] = 1

    for letter in box_dict:
        if (box_dict[letter] == 2) and (twice_found == False):
            twice_count += 1
            twice_found = True
        elif (box_dict[letter] == 3) and (three_found == False):
            three_count += 1
            three_found = True
    twice_found = False
    three_found = False

print(twice_count*three_count)

