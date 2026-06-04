#include <iostream>
using namespace std;

void binary_calc(int n){
    int binary =0,rev=0;

    while(n > 0){
        binary = n%2;
        rev = (rev*10) + binary;
        cout << binary<< " ";
        n /= 2;
    }

}
int main(){
    binary_calc(8);

    return 0;
}
