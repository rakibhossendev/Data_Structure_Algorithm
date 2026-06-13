/*
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *

*/


#include <iostream>
using namespace std;

int main(){
    int n =4;

    for(int i =0; i <n; i++){
        for(int j =0; j<i+1; j++){
            cout << "* ";
        }

        for(int j =0; j <2*(2*n-i)-9; j++){
            cout << " ";
        }
        for(int j =0; j <n-i; j++){
            cout << "* ";
        }

        cout << endl;
    }


    return 0;
}
