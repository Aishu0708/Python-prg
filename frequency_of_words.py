import operator
text_line = input("Type in: ")
freq_dict = {}
for i in text_line.split(' '):
    if i.isalpha():
        if i not in freq_dict:
            freq_dict[i] = 1
        elif i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
    else:
        pass
sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
print(sorted_freq_dict)
for i in sorted_freq_dict:
    print(i[0], i[1])
