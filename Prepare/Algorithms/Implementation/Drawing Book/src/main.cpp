#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'pageCount' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER p
 */

int pageCount(int n, int p) {
    int pageIni = 1;
    int pageFim = n;
    int turnedPagesfromIni = 0;
    int turnedPagesfromFim = 0;
    
    //1->2, 1->3: 1
    //1->4, 1->5: 2
    //1->6, 1->7: 3
    
    for (int i = 0; i < n; i+=2)
    {
        if (p == pageIni +1+i || p == pageIni +2+i)
        {
            turnedPagesfromIni = turnedPagesfromIni+1+(i/2);
        }    
    }
    
    //cout << "turnedPagesfromIni: " << turnedPagesfromIni << "\n";
    
    //cout << "n % 2: " << n % 2 << "\n";
    
    if (n % 2 == 0)                 // se for par
    {
        for (int i = 0; i < n; i+=2)
        {
            //cout << "i: " << i << "\n";
            if (p == pageFim -1-i || p == pageFim -2-i)
            {
                //cout << "turnedPagesfromFim ANTES: " << turnedPagesfromFim << "\n";
                turnedPagesfromFim = turnedPagesfromFim+1+(i/2);
                //cout << "turnedPagesfromFim DEPOIS: " << turnedPagesfromFim << "\n";
            }
        }    
    }
    else
    {
        for (int i = 0; i < n; i+=2)
        {
            //cout << "i: " << i << "\n";
            //cout << "pageFim-1: " << pageFim-1 << "\n";
            //cout << "pageFim -2-i: " << pageFim -2-i << "\n";
            //cout << "pageFim -3-i: " << pageFim -3-i << "\n";
            if ((p != pageFim-1) && (p == pageFim -2-i || p == pageFim -3-i))
            {
                //cout << "turnedPagesfromFim ANTES: " << turnedPagesfromFim << "\n";
                turnedPagesfromFim = turnedPagesfromFim+1+(i/2);
                //cout << "turnedPagesfromFim DEPOIS: " << turnedPagesfromFim << "\n";
            }
        }    
        
    }
    
    /*
    7->6 : 0
    7->5 : 1
    7->4 : 1
    7->3 : 2
    7->2 : 2
    */
    
    
    //cout << "turnedPagesfromFim: " << turnedPagesfromFim;
    
    return min(turnedPagesfromIni, turnedPagesfromFim);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string p_temp;
    getline(cin, p_temp);

    int p = stoi(ltrim(rtrim(p_temp)));

    int result = pageCount(n, p);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
