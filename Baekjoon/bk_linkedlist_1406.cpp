#include<iostream>
#include<list>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string X;
    getline(cin,X);
    int N;
    cin>>N;

    list<char> tfile;
    list<char>::iterator cursor;


    for( auto c : X) tfile.push_back(c);

    cursor=tfile.end();

    for(int i=0; i<N;i++){
        char key;
        cin>>key;
        if(key=='L'){
            if(cursor!=tfile.begin()){
                cursor--;
            }
        }  
        else if(key=='D'){
            if(cursor!=tfile.end()){
                cursor++;
            }
        }
        else if(key=='B'){
            if(cursor!=tfile.begin()){
                cursor--;
                cursor=tfile.erase(cursor);
            }
        }
        else{
            char opt;
            cin>>opt;
            tfile.insert(cursor,opt);
        }      
    }

    for (auto c : tfile) cout<<c;

    return 0;
    
}