import itertools 
import copy
import numpy
#######################################################
#         Decoder that takes from SWE file and 
#       populates list and variables accordingly 
#######################################################

f = open("tests/test07.swe", "r")
k = int(f.readline())
s = f.readline().strip()
t_strings = []
for x in range(0, k):
    t_strings.append(f.readline().strip())
myline = f.readline().strip()
dict_of_R = {}
unused_Rs = []
while(myline):
    tmp_line = myline.split(":")
    unused_Rs.append(tmp_line[0])
    tmp_list_items = tmp_line[1].split(",")
    tmp_list = []
    for x in tmp_list_items:
        tmp_list.append(x)
    dict_of_R[tmp_line[0]] = tmp_list
    myline = f.readline().strip()
f.close()

unused_Rs_copy = copy.deepcopy(unused_Rs)

res = set([s[i: j] for i in range(len(s))
       for j in range(i + 1, len(s) + 1)])

t_strings_copy = list(dict.fromkeys(t_strings))
t_strings_new = copy.deepcopy(t_strings_copy)

t_strings_copy.sort(key=len, reverse=False)
for n in t_strings_copy:
    for m in range(0, len(t_strings_copy)):
        if n in t_strings_copy[m]:
            if n != t_strings_copy[m]:
                if n in t_strings_new:
                    t_strings_new.remove(n)

print("t_strings: {}".format(t_strings_new))



#######################################################
#      Algorithm that is used to find if soultion
#    exists and returns it if it does otherwise NO
#######################################################

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
            tmp_dict_list = dict_of_R[x[i]]
            tmp_dict_list_len = len(tmp_dict_list)
            tmp_index_list = []
            for j in range(0, tmp_dict_list_len):
                if tmp_dict_list[j] not in res:
                    tmp_index_list.append(j)
            tmp_index_list.sort(reverse=True)
            for m in tmp_index_list:
                tmp_dict_list.pop(m)
            dict_of_R[x[i]] = tmp_dict_list

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


def check_substring(t_strings_new, big_Rs, choices, s, all_dicts):
    for choice in choices:
        dmy_len = len(t_strings_new)
        counter = 0
        for x in t_strings_new:
            current_t_string = expansion(x, big_Rs, choice)
            if current_t_string not in res:
                break
            else:
                counter += 1 
        if counter == dmy_len:
            for x in unused_Rs_copy:
                if x in big_Rs:
                    indx = big_Rs.index(x)
                    print("{}: {}".format(x, choice[indx]))
                else:
                    print("{}: {}".format(x, dict_of_R_copy[x]))
            return
    print("NO")
    

dictionary_items = dict_of_R.items()
all_lists = []
for item in dictionary_items:
    all_lists.append(numpy.array(item[1]))

def listoflists(all_lists1, t_string, used_R, s):
    tmp_all_choices = []
    count_t_strings = len(t_string)
    outer_counter = 0
    for x in itertools.product(*all_lists1):
        counter = 0
        for y in t_string:
            current_t_string = expansion(y, used_R, x)
            if current_t_string not in res:
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
        print(outer_counter, end='\r')
        outer_counter+=1
    print('NO')
    #return list(itertools.product(*all_lists1))
    #return tmp_all_choices

def listoflists1(all_lists1, t_string, used_R, s):
    all_choices = []
    for x in itertools.product(*all_lists1):
        dummy_word = expansion(t_string[0], used_R, x)
        if dummy_word in res:
            all_choices.append(x)
    #return list(itertools.product(*all_lists1))
    return all_choices

def cartesian_product(arrays):
    la = len(arrays)
    dtype = numpy.result_type(*arrays)
    arr = numpy.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(numpy.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

t_strings_new.sort(key=len, reverse=True)
used_R.sort()

all_lists_new = cartesian_product(all_lists)

#all_choices = listoflists1(all_lists, t_strings_new, used_R, s)
#listoflists(all_lists, t_strings_new, used_R, s)

print("length of all choices: {}".format(len(all_lists_new)))

check_substring(t_strings_new, used_R, all_lists_new, s, dict_of_R_copy)
