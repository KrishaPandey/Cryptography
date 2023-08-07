#include <iostream>
#include <cstring>
using namespace std;
 

string encrypt(string text, int key)
{
    string result = "";
 
    for (int i = 0; i < text.length(); i++) {
        
        if (isupper(text[i]))
            result += char(int(text[i] + key - 65) % 26 + 65);
            
        else if (isspace(text[i]))
          result+=" ";
 

        else
            result += char(int(text[i] + key - 97) % 26 + 97);
    }
 

    return result;
}

string decrypt(string encryption, int key)
{
    string result = "";
 
    for (int i = 1; i < encryption.length()+1; i++) {
        
        if (isupper(encryption[i]))
            result += char(int(encryption[i] - key - 65) % 26 + 65);
            
        else if (isspace(encryption[i]))
          result+=" ";

        else
            result += char(int(encryption[i] - key - 97) % 26 + 97);
    }
 
    return result;
}

 

int main()
{
    string text = "Krisha Pandey";
    int key = 5;
     string encryption =encrypt(text, key);
    cout<<encryption<<endl;
    string decryption=decrypt( encryption,  key);
    cout<<decryption;
}

