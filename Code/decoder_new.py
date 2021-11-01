from itertools import cycle, product, tee, islice
import copy
import sys
import numpy
import math
import random
#######################################################
#         Decoder that takes from input and 
#       populates list and variables accordingly 
#######################################################
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z']
capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
try:
    k = int(sys.stdin.readline())
except Exception as e:
    print('NO')
    sys.exit()

s = sys.stdin.readline().strip()
for ch in s:
    if ch not in letters:
        print('NO')
        sys.exit()

used_R =[]
t_strings = []
if k < 1:
    print('NO')
    sys.exit()
for x in range(0, k):
    t_strings.append(sys.stdin.readline().strip())
    if(':' in t_strings[x]):
        print('NO')
        sys.exit()
    for cha in t_strings[x]:
        if cha not in letters and cha not in capitalLetters:
            print('NO')
            sys.exit()
        else: 
            if cha.isupper():
                if cha not in used_R:
                    used_R.append(cha)
myline = sys.stdin.readline().strip()
dict_of_R = {}
unused_Rs = []
unused_Rs_copy = []

try:
    while(myline):
        if myline[0] in capitalLetters:
            if myline[1] == ':':
                tmp_line = myline.split(":")
                unused_Rs.append(tmp_line[0])
                unused_Rs_copy.append(tmp_line[0])
                tmp_list_items = tmp_line[1].split(",")
                tmp_list = []
                for x in tmp_list_items:
                    if x in s:
                        tmp_list.append(x)
                dict_of_R[tmp_line[0]] = tmp_list
                myline = sys.stdin.readline().strip()                
            else: 
                print('NO')
                sys.exit()
                myline = sys.stdin.readline().strip()
        else:
            print('NO')
            sys.exit()
            myline = sys.stdin.readline().strip()
except Exception as e:
    print('NO')
    sys.exit()

# Heuristic where every t string that is multiple times or 
# if a t string is a proper substring of another, we eliminate 
# it from the list of strings since we can always find a 
# solution if we just find a solution for the remaining strings

t_strings_copy = list(dict.fromkeys(t_strings))
t_strings_new = copy.deepcopy(t_strings_copy)

t_strings_copy.sort(key=len, reverse=False)
for n in t_strings_copy:
    for m in range(0, len(t_strings_copy)):
        if n in t_strings_copy[m]:
            if n != t_strings_copy[m]:
                if n in t_strings_new:
                    t_strings_new.remove(n)

# Lets start by cutting out all r elements in each R by checking 
# if they alone are a substring of s thus eliminating all r's that
# could never form a substring of s and also get rid of all R that 
# are unused (never appear in any of our t strings)
try:
    dict_of_R_copy = {}
    for element in dict_of_R.keys():
        dict_of_R_copy[element]=dict_of_R[element][0]
    for x in t_strings_new:
        tmp_len = len(x)
        for i in range(0, tmp_len):
            if x[i].isupper():
                if x[i] in unused_Rs:
                    unused_Rs.remove(x[i])
                if x[i] in dict_of_R.keys():
                    tmp_dict_list = dict_of_R[x[i]]
                else:
                    print("NO")
                    sys.exit()
except Exception as e:
    print("NO")
    sys.exit()

for x in unused_Rs:
    del dict_of_R[x]

# function that takes in t_string and a choice of r's and performs 
# expansion on string
def expansion(curr_string, big_Rs, choice):
    new_string = ""
    for c in curr_string:
        if c.isupper():
            tmpindex = big_Rs.index(c)
            new_string += choice[tmpindex]
        else: 
            new_string += c       
    return new_string


# Removing empty string elements from our dictionary and also 
# checking if there exists an empty dictionary in our used
# dictionarys.
dictionary_items = dict_of_R.items()
all_lists = []
for item in dictionary_items:
    if "" in item[1]:
        item[1].remove("")
    if len(item[1]) < 1:
        print('NO')
        sys.exit()
    all_lists.append(numpy.array(item[1]))

#######################################################
#      Algorithm that is used to find if soultion
#    exists and returns it if it does otherwise NO
#######################################################
def find_solution(all_lists1, t_string, used_R, s):
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

# order the t strings from biggest to smallest to eliminate 
# more chioces in the beginning
t_strings_new.sort(key=len, reverse=True)
used_R.sort()

find_solution(all_lists, t_strings_new, used_R, s)
