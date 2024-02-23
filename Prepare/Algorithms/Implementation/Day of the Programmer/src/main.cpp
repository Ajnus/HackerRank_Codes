#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'dayOfProgrammer' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER year as parameter.
 */
 
string addLeadingZero(int num) {
    if (num < 10) {
        return "0" + to_string(num);
    } else {
        return to_string(num);
    }
}

string dayOfProgrammer(int year) {
    int day = 0;
    int month = 9;
    
    
    if (year < 1918)
    {
        if (year % 4 == 0)
        {
            day = 256 - ( 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31);
        }
        else
        {
            day = 256 - ( 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31);
        }      
    }
    else
    {
        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
        {
            day = 256 - ( 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31);
        }
        else
        {
            day = 256 - ( 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31);
        }
        
        if (year == 1918)
        {
            day+=13;
        }
    }
    
    string dayString = addLeadingZero(day);
    string monthString = addLeadingZero(month);
    
    std::string result = dayString+"."+monthString+"."+std::to_string(year);
    return result;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string year_temp;
    getline(cin, year_temp);

    int year = stoi(ltrim(rtrim(year_temp)));

    string result = dayOfProgrammer(year);

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
