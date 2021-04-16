#include<iostream>
#include<stack>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin>>N;
    stack<int> arr;

    for(int i=0;i<N;i++){
        string cmd;
        cin>>cmd;
        if(cmd=="push"){
            int X;
            cin>>X;
            arr.push(X);
        }
        else if(cmd=="top"){
            if(arr.empty()) cout<<-1;
            else cout<<arr.top();
            cout<<'\n';
        }
        else if(cmd=="pop"){
            if(arr.empty()) cout<<-1;
            else{
                cout<<arr.top();
                arr.pop();
            } 
            cout<<'\n';
        }
        else if(cmd=="size") cout<<arr.size()<<'\n';
        else if(cmd=="empty") cout<<arr.empty()<<'\n';
        else{
            cout<<"잘못된입력";
            break;
        }
    }

    return 0;
}