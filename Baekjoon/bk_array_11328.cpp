#include<iostream>
using namespace std;

int Array[26];

int main(){
    ios::sync_with_stdio;
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N ;
    bool check;
    string x,y;
    for(int i=0; i<N; i++){
        cin>>x>>y;
        
        check=true;

        fill(Array, Array + 26, 0);
        if(x.length()!=y.length()){
            cout<<"Impossible\n";
            continue;
        }
        for(int j=0; j<y.length(); j++)
        {
            Array[x[j]-'a']++;
            Array[y[j]-'a']--;
        }
        for(int i=0;i<26;i++){
            if(Array[i]!=0){
                check=false;
                break;
            }
        }
        if(check){
            cout<<"Possible\n";
        }
        else{
            cout<<"Impossible\n";
        }
    }

    return 0;
}