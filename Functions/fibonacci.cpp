#include <iostream>
using namespace std;
int fibonacci(int n){
    int l = 1;
    int r = 1;
    int fibo = 0;

    if(n == 1 || n == 2){
        return 1;
    }

    for(int i=3; i<=n; i++){
        fibo = l + r;
        l = r;
        r = fibo;
    }

    return fibo;
}

int main(){
    int x = fibonacci(4);

    cout << x << endl;

}
