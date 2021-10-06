#######################################################
#         Decoder that takes from SWE file and 
#       populates list and variables accordingly 
#######################################################

f = open("tests/test04.swe", "r")
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


#######################################################
#      Algorithm that is used to find if soultion
#    exists and returns is if it does otherwise NO
#######################################################

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
for item in dictionary_items:
    print(item)
