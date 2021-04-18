#include<iostream>
#include<deque>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin>>N;

    deque<int> DQ;
    
    for(int i=0;i<N;i++){
        string cmd;
        cin>>cmd;
        if(cmd=="push_back"||cmd=="push_front"){
            int add;
            cin>>add;
        
            if(cmd=="push_back"){
                DQ.push_back(add);
            }
            else if(cmd=="push_front"){
                DQ.push_front(add);
            }
        }
        else if(cmd=="pop_front"){
            if(!DQ.empty()){
                cout<<DQ.front();
                DQ.pop_front();
            } 
            else cout<<-1;
            cout<<'\n';
        }
        else if(cmd=="pop_back"){
            if(!DQ.empty()){
                cout<<DQ.back();
                DQ.pop_back();
            } 
            else cout<<-1;
            cout<<'\n';
        }
        
        else if(cmd=="front"){
            if(!DQ.empty()) cout<<DQ.front();
            else cout<<-1;
            cout<<'\n';
        }
        else if(cmd=="back"){
            if(!DQ.empty()) cout<<DQ.back();
            else cout<<-1;
            cout<<'\n';
        }
        else if(cmd=="size") cout<<DQ.size()<<'\n';
        else if(cmd=="empty") cout<<DQ.empty()<<'\n';
        
        else{
            cout<<"잘못된 입력";
            break;
        }
    }

    return 0;
}