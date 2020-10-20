#include <iostream>
#include <cmath>

using namespace std;

void func(double x) {
    double y = 10 + pow(x, 2) - 10*cos(2*3.14*x);
    cout<<"        y = "<<y<<endl;
} 

int main() {
  cout << "Programm started:\n";
  while (true) {
  cout << "\nВведите x = ";
  double x;
  cin>>x;
  func(x);
  }
  return 0;
}
