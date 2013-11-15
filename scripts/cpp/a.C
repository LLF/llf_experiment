#include <iostream>

using namespace std;
union u1
{
    int num1;
    long num2;
    double num3;
};

enum spectrum {red, orange, yellow, green, blue, violet, indigo};


int main(){
    int * pointer;
    *pointer = 2;
    spectrum color = blue;
    cout << color;

    cout << "AA";
    cout << std::endl;
    return 0;
}
