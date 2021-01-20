#include<iostream>
using namespace std;

void convert(string word);

int main(){
    int n;
    string word;

    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> word;
        convert(word);
        cout<< endl;
    }
    return 0;
}

void convert(string word){
    if (word.length() <= 10){
        cout << word;
        return;
    }

    int between = word.length() - 2;
    string result = "";
    result += word[0];
    result += to_string(between);
    result += word[between+1];
    cout << result;
    return;
}