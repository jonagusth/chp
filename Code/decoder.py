from itertools import cycle, product, tee, islice
import copy
import numpy
import operator
import time
import random
#######################################################
#         Decoder that takes from SWE file and 
#       populates list and variables accordingly 
#######################################################
start_time = time.time()
f = open("tests/test06.swe", "r")
k = int(f.readline())
s = f.readline().strip()
t_strings = []
for x in range(0, k):
    t_strings.append(f.readline().strip())
myline = f.readline().strip()
dict_of_R = {}
unused_Rs = []
unused_Rs_copy = []
while(myline):
    tmp_line = myline.split(":")
    unused_Rs.append(tmp_line[0])
    unused_Rs_copy.append(tmp_line[0])
    tmp_list_items = tmp_line[1].split(",")
    tmp_list = []
    for x in tmp_list_items:
        if x in s:
            tmp_list.append(x)
    dict_of_R[tmp_line[0]] = tmp_list
    myline = f.readline().strip()
f.close()

t_strings_copy = list(dict.fromkeys(t_strings))
t_strings_new = copy.deepcopy(t_strings_copy)

t_strings_copy.sort(key=len, reverse=False)
for n in t_strings_copy:
    for m in range(0, len(t_strings_copy)):
        if n in t_strings_copy[m]:
            if n != t_strings_copy[m]:
                if n in t_strings_new:
                    t_strings_new.remove(n)

# Lets start by cutting out all r elements in each R by checking if they alone are a substring of s
# thus eliminating all r's that could never form a substring of s
# and also get rid of all R that are unused (never appear in any of our t strings)
dict_of_R_copy = {}
for element in dict_of_R.keys():
    dict_of_R_copy[element]=dict_of_R[element][0]
used_R =[]
for x in t_strings_new:
    tmp_len = len(x)
    for i in range(0, tmp_len):
        if(x[i].isupper()):
            if x[i] in unused_Rs:
                unused_Rs.remove(x[i])
            if x[i] not in used_R:
                used_R.append(x[i])
for x in unused_Rs:
    del dict_of_R[x]


def expansion(curr_string, big_Rs, choice):
    new_string = ""
    for c in curr_string:
        if c.isupper():
            tmpindex = big_Rs.index(c)
            new_string += choice[tmpindex]
        else: 
            new_string += c       
    return new_string
    

dictionary_items = dict_of_R.items()
all_lists = []
for item in dictionary_items:
    if "" in item[1]:
        item[1].remove("")
    all_lists.append(numpy.array(item[1]))


#######################################################
#      Algorithm that is used to find if soultion
#    exists and returns it if it does otherwise NO
#######################################################
def listoflists(all_lists1, t_string, used_R, s):
    count_t_strings = len(t_string)
    for x in product(*all_lists1):
        counter = 0
        for y in t_string:
            current_t_string = expansion(y, used_R, x)
            if current_t_string not in s:
                break
            else:
                counter += 1 
        if counter == count_t_strings:
            for d in unused_Rs_copy:
                if d in used_R:
                    indx = used_R.index(d)
                    print("{}: {}".format(d, x[indx]))
                else:
                    print("{}: {}".format(d, dict_of_R_copy[d]))
            return
    print('NO')

t_strings_new.sort(key=len, reverse=True)
used_R.sort()

listoflists(all_lists, t_strings_new, used_R, s)

print("--- {:.2f} seconds ---".format(time.time() - start_time))

