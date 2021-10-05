#######################################################
#         Decoder that takes from input and 
#       populates list and variables accordingly 
#######################################################
k = int(input())
s = input().strip()
t_strings = []
for x in range(0, k):
    t_strings.append(input().strip())
myline = input().strip()
dict_of_R = {}
while(myline):
    tmp_line = myline.split(":")
    tmp_list_items = tmp_line[1].split(",")
    tmp_list = []
    for x in tmp_list_items:
        tmp_list.append(x)
    dict_of_R[tmp_line[0]] = tmp_list
    myline = input().strip()

#TODO laga þannig að ef input ekki rétt þá skila NO

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
