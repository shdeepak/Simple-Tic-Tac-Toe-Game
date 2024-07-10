#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<string> b = {"0", "1", "2", "3", "4", "5", "6", "7", "8"};

void displayBoard() {
    cout <<"\t\t" << (b[0] == "X" || b[0] == "O" ? b[0] : "0") << " | "
         << (b[1] == "X" || b[1] == "O" ? b[1] : "1") << " | "
         << (b[2] == "X" || b[2] == "O" ? b[2] : "2") << endl;
    cout <<"\t\t" << (b[3] == "X" || b[3] == "O" ? b[3] : "3") << " | "
         << (b[4] == "X" || b[4] == "O" ? b[4] : "4") << " | "
         << (b[5] == "X" || b[5] == "O" ? b[5] : "5") << endl;
    cout <<"\t\t" << (b[6] == "X" || b[6] == "O" ? b[6] : "6") << " | "
         << (b[7] == "X" || b[7] == "O" ? b[7] : "7") << " | "
         << (b[8] == "X" || b[8] == "O" ? b[8] : "8") << endl;
}

void playerTurn(string ply) {
    cout << "\t\t" << "(" << ply << "'s turn)" << endl;
    cout << "Choose a position from 0-8: ";
    int pos;
    cin >> pos;
    while (pos < 0 || pos > 8 || (b[pos] == "X" || b[pos] == "O")) {
        cout << "Error!!! Wrong position selected. Choose a position from 0-8: ";
        cin >> pos;
    }
    b[pos] = ply;
    displayBoard();
}

string checkOver() {
    if ((b[0] == b[1] && b[1] == b[2]) ||
        (b[3] == b[4] && b[4] == b[5]) ||
        (b[6] == b[7] && b[7] == b[8]) ||
        (b[0] == b[3] && b[3] == b[6]) ||
        (b[1] == b[4] && b[4] == b[7]) ||
        (b[2] == b[5] && b[5] == b[8]) ||
        (b[0] == b[4] && b[4] == b[8]) ||
        (b[2] == b[4] && b[4] == b[6])) {
        return "Win";
    } else if (count(b.begin(), b.end(), "X") + count(b.begin(), b.end(), "O") == 9) {
        return "Tie";
    } else {
        return "Play";
    }
}

int main() {
    cout<<"Welcome to Tic-Tac-Toe Game!"<<endl;
    cout<<"\n";
    displayBoard();
    string curr = "X";
    bool Over = false;
    while (!Over) {
        playerTurn(curr);
        string Result = checkOver();
        if (Result == "Win") {
            cout << curr << " Wins!" << endl;
            Over = true;
        } else if (Result == "Tie") {
            cout << "It's a tie!" << endl;
            Over = true;
        } else {
            curr = (curr == "X") ? "O" : "X";
        }
    }
    return 0;
}
