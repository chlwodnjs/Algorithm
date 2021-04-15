#include<iostream>
#include<list>

using namespace std;

int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,K;
    cin>>N>>K;

    list<int> circle;
    list<int>::iterator cursor;

    for(int i=0; i<N; i++){
        circle.push_back(i+1);
    }
    
    cursor=circle.begin();
    
    for(int i=1; i<K; i++){
        cursor++;
    }

    cout<<'<';
    
    while(N>1){
        cout<<*cursor<<", ";
        cursor=circle.erase(cursor);

        if(cursor == circle.end()){
            cursor = circle.begin();
        }
        
        for(int i=1; i<K;i++){
            cursor++;
            if(cursor == circle.end()){
                cursor=circle.begin();
            }
        }
        N--;
    }

    for(auto c : circle) cout<<c;
    cout<<'>';

    return 0;
    
}