#include <iostream>
#include <cmath>
using namespace std;

void func(double x) {
    double y = 0.5 + (pow(sin(pow(x, 2)), 2) - 0.5)/pow ((1 + 0.001*(pow(x, 2))), 2);
    cout << x << "      " << round(y*100)/100 << "\n";
    //return y;
}

int main() {
    cout<<"X         Y\n";
    for (double x = -10; x <=10; x = x + 0.5) {
        func(x);
    }
    return 0;
}
