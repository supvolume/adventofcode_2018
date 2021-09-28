txt = open("day05_input.txt", "r").read()
#txt = open("day05_test_input.txt", "r").read()

def remove_up_low(text):
    keep_text = []
    found = False
    count = 0
    while found == False and count < len(text)-1:
        if ((text[count].isupper() != text[count+1].isupper()) and \
           (text[count].lower() == text[count+1].lower())):
            found = True
            break
        else:
            keep_text.append(text[count])
        count += 1
    if found == False:
        return text
    else:
        return "".join(keep_text) + text[count+2:]

  
# Part 1
def polymer_loop(txt):
    len_eq = False
    while len_eq == False:
        n = len(txt)
        txt = remove_up_low(txt)
        if n == len(txt):
            len_eq = True
    return txt

# Part 1 answer
#print(len(polymer_loop(txt)))


# Part 2
alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet = "abcd"
all_len = []
for i in alphabet:
    print(i)
    re_text = txt.replace(i, "")
    re_text = re_text.replace(i.upper(), "")
    all_len.append(len(polymer_loop(re_text)))

print(sorted(all_len))

