#include <iostream>
using namespace std;

class Complex
{

	int real;
	int img;

public:
	Complex()
	{
		real = 0;
		img = 0;
	}

	Complex operator+(Complex c2)
	{
		Complex temp;
		temp.real = real + c2.real;
		temp.img = img + c2.img;
		return temp;
	}

	Complex operator*(Complex c2)
	{
		Complex temp;
		temp.real = (real * c2.real) - (img * c2.img);
		temp.img = (img * c2.real) + (real*c2.img);
		return temp;
	}

	friend istream &operator>>(istream &din, Complex &c3)
	{
		din >> c3.real >> c3.img;
		return din;
	}

	friend ostream &operator<<(ostream &dout, Complex &c3)
	{
		dout << "\n"<< c3.real << " + " << c3.img << "i" << endl;
		return dout;
	}
};

int main()
{

	Complex c1, c2,add,mul;

	cout<<"Enter First Complex Number(Real and Img):";
	cin>>c1;

	cout<<"Enter Second Complex Number(Real and Img):";
	cin>>c2;


	cout<<"Addition of Two Complex Numbers:";
	add = c1+c2;
	cout << add;

	cout<<"Multiplication of Two Complex Numbers:";
	mul = c1*c2;
	cout<<mul;

	return 0;
}
