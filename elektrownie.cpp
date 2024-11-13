#include <bits/stdc++.h>
using namespace std;

const int N = 6;
const int M = 4;  

class weather 
{
    public:
        string type;
        bool active;
};

class elektrownia 
{
    public:
        string type;
        bool active;
        int eko;
        int koszt;
        int dlugo;
};

int ocen_efektywnosc(const elektrownia &e, const weather &w) 
{
    if (e.type == "solarna") 
	{
        if (w.type == "sundy") return 10;   
        if (w.type == "windy") return 6;   
        if (w.type == "cloudy") return 3;    
        if (w.type == "rainy") return 2;    
    }
    else if (e.type == "wiatrowa") 
	{
        if (w.type == "windy") return 10;   
        if (w.type == "cloudy") return 7;   
        if (w.type == "sundy") return 5;    
        if (w.type == "rainy") return 5;    
    }
    else if (e.type == "wodna") 
	{
        if (w.type == "rainy") return 9;    
        if (w.type == "cloudy") return 7;   
        if (w.type == "windy") return 6;    
        if (w.type == "sundy") return 4;    
    }
    else if (e.type == "atomowa") 
	{
        if (w.type == "sundy") return 7;
        if (w.type == "cloudy") return 7;
        if (w.type == "windy") return 7;
        if (w.type == "rainy") return 7;
    }
    else if (e.type == "weglowa") 
	{
        if (w.type == "cloudy") return 8;
        if (w.type == "rainy") return 7;
        if (w.type == "windy") return 5;
        if (w.type == "sundy") return 3;
    }
    else if (e.type == "gazowa") 
	{
        if (w.type == "sundy") return 8;
        if (w.type == "windy") return 7;
        if (w.type == "rainy") return 5;
        if (w.type == "cloudy") return 3;
    }
    return 3; 
}

int main() 
{
    elektrownia tab[N];
    tab[0].type = "wiatrowa";
    tab[1].type = "wodna";
    tab[2].type = "weglowa";
    tab[3].type = "atomowa";
    tab[4].type = "gazowa";
    tab[5].type = "solarna";
    
    tab[0].eko = 8;
    tab[1].eko = 7;
    tab[2].eko = 3;
    tab[3].eko = 10;
    tab[4].eko = 5;
    tab[5].eko = 7;
    
    tab[0].koszt = 3;
    tab[1].koszt = 5;
    tab[2].koszt = 6;
    tab[3].koszt = 10;
    tab[4].koszt = 7;
    tab[5].koszt = 2;
    
    tab[0].dlugo = 3;
    tab[1].dlugo = 6;
    tab[2].dlugo = 7;
    tab[3].dlugo = 10;
    tab[4].dlugo = 3;
    tab[5].dlugo = 6;
    
    weather weathers[M];
    weathers[0].type = "sundy";
    weathers[1].type = "cloudy";
    weathers[2].type = "windy";
    weathers[3].type = "rainy";

    for(int i = 0; i < N; i++) 
	{
        for(int j = 0; j < M; j++) 
		{
            int k = ocen_efektywnosc(tab[i], weathers[j]);
            cout << "Efektywnosc pracy elektrowni " << tab[i].type << " przy pogodzie " << weathers[j].type << " wynosi: " << k << "/10" << endl;
        }
        cout << endl;
    }

    return 0;
}


