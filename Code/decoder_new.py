import itertools 
import copy
import sys
import numpy
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
        print('NO')
        sys.exit()
s = sys.stdin.readline().strip()
for ch in s:
    if ch not in letters:
        print('NO')
        sys.exit()
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
myline = sys.stdin.readline().strip()
dict_of_R = {}
unused_Rs = []

#try:
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
            print('NO')
            sys.exit()
            myline = sys.stdin.readline().strip()
    else:
        print('NO')
        sys.exit()
        myline = sys.stdin.readline().strip()

#except IndexError:
#    print('NO')
#    sys.exit()

unused_Rs_copy = copy.deepcopy(unused_Rs)

#if(len(valid_input) > 0):
    #print(valid_input)
    #sys.exit()

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

#######################################################
#      Algorithm that is used to find if soultion
#    exists and returns it if it does otherwise NO
#######################################################
import math

class LazyCartesianProduct:
    def __init__(self, sets):
        self.sets = sets
        self.divs = []
        self.mods = []
        self.maxSize = 1
        self.precompute()
    
    def precompute(self):
        for i in self.sets:
            self.maxSize = self.maxSize * len(i)
        length = len(self.sets)
        factor = 1
        for i in range((length - 1), -1, -1):
            items = len(self.sets[i])
            self.divs.insert(0, factor)
            self.mods.insert(0, items)
            factor = factor * items
    
    def entryAt(self, n):
        length = len(self.sets)
        if n < 0 or n >= self.maxSize:
            raise IndexError
        combination = []
        for i in range(0, length):
            combination.append(self.sets[i][ int(math.floor(n / self.divs[i])) % self.mods[i]])
        return combination

# Lets start by cutting out all r elements in each R by checking if they alone are a substring of s
# thus eliminating all r's that could never form a substring of s
# and also get rid of all R that are unused (never appear in any of our t strings)
#error hér

#try:
dict_of_R_copy = {}
for element in dict_of_R.keys():
    dict_of_R_copy[element]=dict_of_R[element][0]
used_R =[]
for x in t_strings_new:
    tmp_len = len(x)
    for i in range(0, tmp_len):
        if x[i].isupper():
            if x[i] in unused_Rs:
                unused_Rs.remove(x[i])
            if x[i] not in used_R:
                used_R.append(x[i])
            if x[i] in dict_of_R.keys():
                tmp_dict_list = dict_of_R[x[i]]
            else:
                print("NO")
                sys.exit()
            tmp_dict_list_len = len(tmp_dict_list)
            tmp_index_list = []
            
            for j in range(0, tmp_dict_list_len):
                if tmp_dict_list[j] not in s:
                    tmp_index_list.append(j)
            tmp_index_list.sort(reverse=True)
            for m in tmp_index_list:
                if len(tmp_dict_list) > 1:
                    tmp_dict_list.pop(m)
            dict_of_R[x[i]] = tmp_dict_list

    
#except OverflowError:
    #print("NO")
    #sys.exit()

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
                    if len(dict_of_R_copy[x])>0:
                        print("{}: {}".format(x, dict_of_R_copy[x]))
                    else:
                        print("{}: {}".format(x, ''))
            return
    print("NO")
    


#error fyrir hérna

# Make a list with all possible choices of r's from used R's and check if there is a solution
dictionary_items = dict_of_R.items()
all_lists = []
for item in dictionary_items:
    if "" in item[1]:
        item[1].remove("")
    if len(item[1]) < 1:
        print('NO')
        sys.exit()
    all_lists.append(numpy.array(item[1]))




def listoflists(all_lists1, t_string, used_R, s):
    count_t_strings = len(t_string)
    for x in itertools.product(*all_lists1):
        counter = 0
        for y in t_strings:
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
    print('NO')

def listoflists1(all_lists1, t_string, used_R, s):
    all_choices = []
    for x in itertools.product(*all_lists1):
        dummy_word = expansion(t_string[0], used_R, x)
        if dummy_word in res:
            all_choices.append(x)
    #return list(itertools.product(*all_lists1))
    return all_choices


# Notar LazyCartesionProduct Klasann
def check_solution(cp, t_string):
    count_t_strings = len(t_string)
    for x in range(0, cp.maxSize):
        counter = 0
        for y in t_string:
            current_t_string = expansion(y, used_R, cp.entryAt(x))
            if current_t_string not in res:
                break
            else:
                counter += 1
        if counter == count_t_strings:
            for d in unused_Rs_copy:
                if d in used_R:
                    indx = used_R.index(d)
                    print("{}: {}".format(d, cp.entryAt(x)[indx]))
                else:
                    print("{}: {}".format(d, dict_of_R_copy[d]))
            return
    print('NO')

#error fyrir þetta

t_strings_new.sort(key=len, reverse=True)
used_R.sort()

#all_choices = listoflists1(all_lists, t_strings, used_R, s)

#listoflists(all_lists, t_strings, used_R, s)

cp = LazyCartesianProduct(all_lists)
check_solution(cp, t_strings_new)


#check_substring(t_strings, used_R, all_choices, s, dict_of_R_copy)