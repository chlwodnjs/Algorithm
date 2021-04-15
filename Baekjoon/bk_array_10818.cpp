#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    ios::sync_with_stdio;
    cin.tie(0);

    int N,num;
    cin>>N;
    vector<int> v;
    for(int i=0; i<N; i++){
        cin>>num;
        v.push_back(num);
    }

    sort(v.begin(),v.end());

    cout<<v[0]<<' '<<v[N-1];

    return 0;

}