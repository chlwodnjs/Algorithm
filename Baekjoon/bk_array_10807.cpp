#include<iostream>
using namespace std;
// int N,X,cnt,Array[100];
int main() {

    ios::sync_with_stdio;
    cin.tie(0);
    int N,X;
    int cnt=0;
    cin>>N;
    int Array[N];
    for(int i=0; i<N; i++){
        cin>>Array[i];
    }
    cin>>X;

    for(int i=0;i<N;i++){
        if(X==Array[i]){
            cnt++;
        }
    }
    
    cout<<cnt<<'\n';

    return 0;
}