#include<iostream>
#include<stack>

using namespace std;

int main(){
    int K;
    cin>>K;
    int sum=0;

    stack<int> numArray;

    for(int i=0;i<K;i++){
        int num;
        cin>>num;

        if(num==0){
            if(!numArray.empty()){
                numArray.pop();
            }
        }
        else{
            numArray.push(num);
        }
        
    }

    while(!numArray.empty()){
        sum+=numArray.top();
        numArray.pop();
    }
    cout<<sum;

    return 0;
}