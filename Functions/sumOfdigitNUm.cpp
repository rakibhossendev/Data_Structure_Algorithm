#include <iostream>
using namespace std;

int sumOfDigit(int n){
    int sum=0,i,digits;

    while(n > 0){
        digits = n % 10;
        sum += digits;

        n /= 10;
    }

    return sum;
}

int main(){
    cout << sumOfDigit(145) << endl;

    return 0;
}
