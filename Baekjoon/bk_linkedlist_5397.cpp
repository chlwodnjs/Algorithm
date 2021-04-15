#include<iostream>
#include<list>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin>>N;

    for(int i=0; i<N; i++){
        string Xword;
        cin>>Xword;

        list<char> tfile;
        list<char>::iterator cursor;
        cursor = tfile.begin();

        for(int key=0; key<Xword.length(); key++){
            if(Xword[key]=='<'){
                if(cursor!=tfile.begin()){
                    cursor--;
                }
            }
            else if(Xword[key]=='>'){
                if(cursor!=tfile.end()){
                    cursor++;
                }
            }
            else if(Xword[key]=='-'){
                if(cursor!=tfile.begin()){
                    cursor=tfile.erase(--cursor);
                }
            }
            else{
                tfile.insert(cursor,Xword[key]);

            }
        }
        for(auto c: tfile){
            cout<<c;
        }
        cout<<'\n';
    }

    return 0;

}

