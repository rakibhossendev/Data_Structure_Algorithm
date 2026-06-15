#include <iostream>
using namespace std;

int binary(int n){
    int power = 1;
    int ans = 0;
    while(n > 0){
        int binary = n % 2;

        ans += (binary * power);
        power *= 10;

        n /= 2;
    }

    return ans;
}

int main(){
    int x = binary(6);
    cout << x;
}
