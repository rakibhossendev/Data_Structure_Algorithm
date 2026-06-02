#include <iostream>
using namespace std;

int factorial(int n){
    int fact = 1;

    for(int i=1; i<=n; i++){
        fact *= i;
    }
    return fact;
}

int binomal(int n,int r){
    int diff = n -r;
    int binomal = factorial(n)/(factorial(r)*factorial(diff));

    return binomal;
}

int main(){
    int n=6,r=3;

    cout << binomal(n,r) << endl;


    return 0;
}
