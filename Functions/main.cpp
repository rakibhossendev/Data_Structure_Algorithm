#include <iostream>
using namespace std;

int fact(int n){
    int fact = 1;

    for(int i = 1; i <=n; i++){
        fact *= i;
    }

    return fact;

}

int sum(int a,int b){
    a = a + 10;
    b = b+10;

    return (a+b);
}


int main(){
    int x=10,y=20;

    cout <<sum(x,y) << endl;

    cout << x << endl;
    cout << y << endl;


    return 0;
}
