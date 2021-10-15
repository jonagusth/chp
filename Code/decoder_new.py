import itertools 
import copy
import sys
#######################################################
#         Decoder that takes from input and 
#       populates list and variables accordingly 
#######################################################
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
valid_input = ''
while True:
    try:
        k = int(sys.stdin.readline())
        break
    except ValueError:
        valid_input = 'NO'
        sys.exit()
#k = int(input())
s = sys.stdin.readline().strip()
t_strings = []
for x in range(0, k):
    t_strings.append(sys.stdin.readline().strip())
    if(':' in t_strings[x]):
        valid_input = 'NO'
myline = sys.stdin.readline().strip()
dict_of_R = {}
unused_Rs = []
while(myline):
    if myline[0] in capitalLetters:
        if myline[1] == ':':
            tmp_line = myline.split(":")
            unused_Rs.append(tmp_line[0])
            tmp_list_items = tmp_line[1].split(",")
            tmp_list = []
            for x in tmp_list_items:
                tmp_list.append(x)
            dict_of_R[tmp_line[0]] = tmp_list
            myline = sys.stdin.readline().strip()                
        else: 
            valid_input = 'NO'
            myline = sys.stdin.readline().strip()
    else:
        valid_input = 'NO'
        myline = sys.stdin.readline().strip()

unused_Rs_copy = copy.deepcopy(unused_Rs)

if(len(valid_input) > 0):
    print(valid_input)
    sys.exit()

#TODO laga þannig að ef input ekki rétt þá skila NO

#######################################################
#      Algorithm that is used to find if soultion
#    exists and returns it if it does otherwise NO
#######################################################

# Lets start by cutting out all r elements in each R by checking if they alone are a substring of s
# thus eliminating all r's that could never form a substring of s
# and also get rid of all R that are unused (never appear in any of our t strings)
dict_of_R_copy = copy.deepcopy(dict_of_R)
used_R =[]
for x in t_strings:
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
                if tmp_dict_list[j] not in s:
                    tmp_index_list.append(j)
            tmp_index_list.sort(reverse=True)
            for m in tmp_index_list:
                tmp_dict_list.pop(m)
            dict_of_R[x[i]] = tmp_dict_list

for x in unused_Rs:
    del dict_of_R[x]


# function that takes in t_string and a choice of r's and performs expansion on string
def expansion(curr_string, big_Rs, choice):
    new_string = ""
    for c in curr_string:
        if c.isupper():
            tmpindex = big_Rs.index(c)
            new_string += choice[tmpindex]
        else: 
            new_string += c       
    return new_string

# Function that takes in all t_strings, and all possible chioces of r's and checks if there 
# exists a choice where all t_strings are a subset of s
def check_substring(t_strings, big_Rs, choices, s, all_dicts):
    for choice in choices:
        dmy_len = len(t_strings)
        counter = 0
        for x in t_strings:
            current_t_string = expansion(x, big_Rs, choice)
            if current_t_string not in s:
                break
            else:
                counter += 1 
        if counter == dmy_len:
            for x in unused_Rs_copy:
                if x in big_Rs:
                    indx = big_Rs.index(x)
                    print("{}: {}".format(x, choice[indx]))
                else:
                    print("{}: {}".format(x, dict_of_R_copy[x][0]))
            return
    print("NO")

# Make a list with all possible choices of r's from used R's and check if there is a solution
dictionary_items = dict_of_R.items()
all_lists = []
for item in dictionary_items:
    all_lists.append(item[1])

all_choices = list(itertools.product(*all_lists))
t_strings.sort(key=len, reverse=True)
used_R.sort()
check_substring(t_strings, used_R, all_choices, s, dict_of_R_copy)