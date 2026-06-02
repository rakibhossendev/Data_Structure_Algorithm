#include <iostream>
using namespace std;

int prime(int n){
    int i = 2;

    while( i *  i <= n){
        if(n%i==0){
            return 0;
        }
        else{
            return 1;
        }

        i += 1;
    }
}

int main(){
    int x = prime(10 );

    if(x == 1){
        cout <<"is prime "<< endl;
    }else{
        cout <<"is not prime"<< endl;
    }

    return 0;
}
