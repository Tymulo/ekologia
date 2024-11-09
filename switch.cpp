#include<bits/stdc++.h>

using namespace std;

int main()
{
	int x;
	srand(time(NULL));
	int a = rand()%10+1;
	cin >> x;
	cout << a << endl;
	switch(x + a)
	{
		case 15:
			cout << "15";
			break;
		case 20:
			cout << "20";
			break;
		case 10:
			cout << "10";
			break;
		case 5:
			cout << "5";
			break;
		default:
			cout << "nie";
			break;
	}
}
