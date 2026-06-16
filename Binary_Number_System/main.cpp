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

int decimal(int number){
    int answer = 0;
    int power = 1;

    while(number > 0){
        int last_digit = number % 10;

        answer += (last_digit *power);
        power *= 2;

        number /= 10;
    }

    return answer;

}
int main(){
    int x = 1100;

    cout << decimal(x) << endl;
}
