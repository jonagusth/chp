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
while(myline):
    tmp_line = myline.split(":")
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

