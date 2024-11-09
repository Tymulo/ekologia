#include <bits/stdc++.h>
using namespace std;
const int N = 4;

class weather
{
    public:
        string type;
        bool active;
};

int losuj_pogode(int x, weather tab[], weather &old_weather)
{
    int w = rand() % 6 + 1;
    if(w > x)
    {
        int n = rand() % 4;
        old_weather.active = false;
        tab[n].active = true;
        x = 6;
    }
    else
    {
        x -= 1;
    }
    return x;
}

int main()
{
    int x = 6;
    weather tab[N];
    tab[0].type = "sundy";
    tab[1].type = "cloudy";
    tab[2].type = "windy";
    tab[3].type = "rainy";
	srand(time(NULL));
    for(int i = 0; i < N; i++)
    {
        tab[i].active = false;
    }
    tab[0].active = true;
    for(int i = 0; i <= 24; i++)
    {
        for(int j = 0; j < N; j++)
        {
            if(tab[j].active)
            {
                x = losuj_pogode(x, tab, tab[j]);
                break;
            }
        }

        for(int j = 0; j < N; j++)
        {
            if(tab[j].active)
            {
                cout << tab[j].type << endl;
                break;
            }    
        }
    }
}
