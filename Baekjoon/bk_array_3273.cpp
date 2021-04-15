#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    ios::sync_with_stdio;
    cin.tie(0);

    int N,X,num;
    int cnt=0;
    cin>>N;
    vector<int> v;

    for(int i=0; i<N; i++){
        cin>>num;
        v.push_back(num);
    }
    
    cin>>X;

    sort(v.begin(),v.end());
    int low=0;
    int high=N-1;

    while(1){
        int check=v[low]+v[high];

        if(low>=high) break;
        if(check==X){
            cnt++;
            low++;
            high--;
        }
        else if(check<X) low++;
        else high--;
    }

    cout<<cnt;

    return 0;
}