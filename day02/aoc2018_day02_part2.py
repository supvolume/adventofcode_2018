txt = open("day02_input.txt", 'r').read()
txt_list = txt.split("\n")

test_list = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

all_correct = dict()

# Remove one letter from word
for i in range(len(txt_list[0])):
    cut_word_list = []
    reduce_dict = dict()
    for word in txt_list:
        cut_word = word[:i]+word[i+1:]
        if cut_word in reduce_dict:
            reduce_dict[cut_word] += 1
            
        else:
            reduce_dict[cut_word] = 1

    # Find the words that have matches in each round
    for k, v in reduce_dict.items():
        if v > 1:
            if k in all_correct:
                all_correct[k] += 1
            else:
                all_correct[k] = 1


        
all_correct = dict(sorted(all_correct.items(), key=lambda item: item[1], reverse=True))
print(list(all_correct.keys())[0])
        
