#include<iostream>
#include<queue>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin>>N;
    
    queue<int> numQ;

    for(int i=0; i<N; i++){
        string cmd;
        cin>>cmd;

        if(cmd=="push"){
            int add;
            cin>>add;
            numQ.push(add);
        }
        else if(cmd=="front"){
            if(!numQ.empty()) cout<<numQ.front();
            else cout<<-1;
            cout<<'\n';
        }
        else if(cmd=="back"){
            if(!numQ.empty()) cout<<numQ.back();
            else cout<<-1;
            cout<<'\n';
        }
        else if(cmd=="size"){
            cout<<numQ.size()<<'\n';
        }
        else if(cmd=="empty"){
            cout<<numQ.empty()<<'\n';
        }
        else if(cmd=="pop"){
            if(!numQ.empty()){
                cout<<numQ.front();
                numQ.pop();
            }
            else cout<<-1;
            cout<<'\n';
        }
        else{
            cout<<"잘못된 명령어";
        }
    }
        return 0;
    
}