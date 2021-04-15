#include<iostream>

using namespace std;

int arr[2][6];

int main(){
    int N,X;
    cin>>N>>X;

    int sex,grade;
    int cnt=0;

    for(int i=0;i<N;i++){
        cin>>sex>>grade;
        arr[sex][grade-1]++;
    }

    for(int i=0;i<2;i++){
        for(int j=0;j<6;j++){
            if(arr[i][j]!=0){
                if(arr[i][j]>X){
                    if(arr[i][j]%X==0) cnt+=arr[i][j]/X;
                    else cnt+=(arr[i][j]/X)+1;
                }
                else{
                    cnt++;
                }
            }
        }
    }
    cout<<cnt;
    return 0;

}