#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int Array[26];

int main(){
    string a,b;
    getline(cin,a);
    getline(cin,b);
    int cnt=0;

    if(a.length()!=0 && b.length()!=0){
        for(int i=0; i<a.length(); i++) Array[a[i]-'a']++;
        for(int j=0; j<b.length(); j++) Array[b[j]-'a']--;
    }
    
    for(int i=0; i<26; i++) cnt+=abs(Array[i]);
    
    cout<<cnt;

    return 0;
}