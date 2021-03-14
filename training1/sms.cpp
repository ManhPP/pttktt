#include<iostream>
using namespace std;

void count(string word, int n);

int main(){
    int n;
    string word;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++){
        getline(cin, word);
        count(word, i+1);
        cout<< endl;
    }
    return 0;
}

void count(string word, int n){
    int result = 0;
    int len = word.length();

    for (int i = 0; i < len; i++){
        char c = word.at(i);
        if (c == 'a' || c == 'd' || c == 'g' || c == 'j' || c == 'm' || c == 'p' || c == 't' || c == 'w' || c == ' '){
            result += 1;
        }
        else if (c == 'b' || c == 'e' || c == 'h' || c == 'k' || c == 'n' || c == 'q' || c == 'u' || c == 'x')
        {
            result += 2;
        }
        else if (c == 'c' || c == 'f' || c == 'i' || c == 'l' || c == 'o' || c == 'r' || c == 'v' || c == 'y')
        {
            result += 3;
        }
        else if (c == 's' || c == 'z')
        {
            result += 4;
        }  
    }

    cout << "Case #" << n << ": " << result;
    return;
}