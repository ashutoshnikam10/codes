#include <iostream>
#include <string>
#include <algorithm> //Provides functions like transform() for text processing

    using namespace std;

// Function to convert string to lowercase

string toLowerCase(string str)
{
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return str;
}

// Function to generate bot responses based on user input 
string generateResponse(const string& userInput) 
{
 string lowerInput =toLowerCase(userInput);

    if(lowerInput.find("hello") != string::npos)
    {
    return "Hi there! How can I assist you today?";

    }else if (lowerInput.find("how are you") != string::npos)
    {
        return "I'm just a program, but thanks for asking!";
    }
    else if (lowerInput.find("bye") != string::npos)
    {

        return "Goodbye! Have a great day!";
    }
    else
    {

        return "I'm not sure I understand. Try asking about something else!";
    }

}

int main()
{

    string userInput;

    cout << "Welcome to ChatBot! Type your message below." << endl;
    cout << "Type 'bye' anytime to exit." << endl;

    while (true)
    {

        cout << "You: ";

        getline(cin, userInput);

        if (toLowerCase(userInput) =="bye")
        {

            cout << "Bot: Goodbye! Have a great day!" << endl;
            break;
        }

        cout << "Bot:" << generateResponse(userInput) << endl;
    }

    return 0;

}