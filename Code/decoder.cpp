#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <cctype>
#include <cstring>
#include <vector>
#include <algorithm>
#include<sstream>

using namespace std;

//string expansion(string curr_string, string big_Rs[], string choice[]){  
//}

int main()
{
    //char letters[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    //char capitalLetters[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    //string valid input = '';

    int k;
    cin >> k;

    string s;
    cin >> s;

    vector<string> t_strings;;
    for(int i = 0; i < k; i++){
        string tmpstr;
        cin >> tmpstr;
        t_strings.push_back(tmpstr);
    }

    vector<string> unused_Rs;
    map<string, vector<string>> dict_of_R;

    while(!cin.fail()){
        string myline;
        cin >> myline;
        vector<string> result;
        stringstream s_stream(myline); //create string stream from the string
        string R;
        getline(s_stream, R, ':');
        unused_Rs.push_back(R);
        while(s_stream.good()) {
            string substr;
            getline(s_stream, substr, ','); //get first string delimited by comma
            result.push_back(substr);
        }
        dict_of_R[R] = result;
    }

    vector<string> unused_Rs_copy = unused_Rs;

    map<string, vector<string>> dict_of_R_copy = dict_of_R;
    vector<string> used_R;

    for (size_t i = 0; i < t_strings.size(); i++){
        int tmp_len = t_strings[i].length();
        for(int j = 0; j < tmp_len; j++){
            if(isupper(t_strings[i][j])){
                if(find(unused_Rs.begin(), unused_Rs.end(), t_strings[i][j]) != unused_Rs.end()){
                    remove(unused_Rs.begin(), unused_Rs.end(), t_strings[i][j]);
                }
                if(!find(used_R.begin(), used_R.end(), t_strings[i][j]) != used_R.end()){
                    used_R.push_back(t_strings[i][j])
                }
                vector<string> tmp_dict_list = dict_of_R[t_strings[i][j]];
                int tmp_dict_list_len = dict_of_R[t_strings[i][j]].size();
                for(int k = 0; k < tmp_dict_list_len; k++){
                    if (s.find(tmp_dict_list[k]) == string::npos) {
                        remove(dict_of_R[t_strings[i][j]].begin(), dict_of_R[t_strings[i][j]].end(), tmp_dict_list[k]);
                    } 
                }
            }
        }
	}

    for(size_t l = 0; l < unused_Rs.size(); l++){
        dict_of_R.erase(unused_Rs[l]);
    }

    cout << dict_of_R << endl;
    
    return 0;
}