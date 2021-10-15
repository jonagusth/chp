#######################################################
#         Decoder that takes from SWE file and 
#       populates list and variables accordingly 
#######################################################

f = open("tests/test02.swe", "r")
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

#########################################################
# print("k er: {}".format(k))
# print("s er: {}".format(s))
# print("t strengirnir okkar eru:",*t_strings, sep=", ")
# dictionary_items = dict_of_R.items()
# for item in dictionary_items:
#     print(item)
##########################################################
from anytree import Node, RenderTree


#######################################################
#      Class used to implement tree structure
#    Of all possible combinations of choices of r
#######################################################
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


#######################################################
#      Algorithm that is used to find if soultion
#    exists and returns it if it does otherwise NO
#######################################################

# Function that constructs a list of dictionaries with all possible cominations of chioces of r from R
def list_of_dicts(dict_items):
    count_of_items = len(dict_items)
    count_of_choices = 1
    for item in dict_items:
        tmp_item_count = len(item[1])
        count_of_choices *= tmp_item_count
    print(count_of_choices)



# Lets start by cutting out all r elements in each R by checking if they alone are a substring of s
# thus eliminating all r's that could never form a substring of s
# and also get rid of all R that are unused (never appear in any of our t strings)
for x in t_strings:
    tmp_len = len(x)
    for i in range(0, tmp_len):
        if(x[i].isupper()):
            if x[i] in unused_Rs:
                unused_Rs.remove(x[i])
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

dictionary_items = dict_of_R.items()
list_of_dicts(dictionary_items)
for item in dictionary_items:
    print(item)


root = [Node([])]
# Function that constructs a tree of all possible choices of r from R
def make_a_tree(parents, children):
    print(*parents)
    for node in parents:
        #print(node.data)
        for y in children:
            tmp_node = Node(y)
            node.add_child(tmp_node)
    return parents

for item in dictionary_items:
    root = make_a_tree(root, item[1])

print(*root)

#for child in root.children:
#    print(child.data)