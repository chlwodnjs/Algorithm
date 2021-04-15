#include<iostream>
using namespace std;
int countArray[26];

int main(){

    string s;
    getline(cin,s);
    for(int j=0; j<s.length(); j++){
        countArray[s[j]-'a']++;
    }
    for(int i =0; i < 26; i++){
        cout<<countArray[i]<<" ";
    }
    
   return 0;
}