#include <iostream>
#include <ctime>
#include <cstdlib>
#include <map>
#include <string>
using namespace std;
const int MAX_VAL = 100;
const int DICE_FACE = 6;

// Node structure for Binary Search Tree
struct Node {
    int key;
    int value;
    Node* left;
    Node* right;

    Node(int key, int value) {
        this->key = key;
        this->value = value;
        left = NULL;
        right = NULL;
    }
};

// Player class representing a player in the game
class Player {
private:
    string name;
    int current_position;

public:
    Player(const string& name) {
        this->name = name;
        current_position = 0;
    }

    string getName() const {
        return name;
    }

    int getCurrentPosition() const {
        return current_position;
    }

    void move(int steps) {
        current_position += steps;
    }
};

// Game class representing the Snakes and Ladders game
class SnakesAndLadders {
private:
    map<int, int> snakes;
    map<int, int> ladders;
    Node* root;
    Player* players[2];

public:
    SnakesAndLadders(const string& player1Name, const string& player2Name) {
        players[0] = new Player(player1Name);
        players[1] = new Player(player2Name);
        root = NULL;

        // Initialize snakes and ladders
        initializeSnakes();
        initializeLadders();
        // Build BST
        buildBST();
    }

    ~SnakesAndLadders() {
        delete players[0];
        delete players[1];
        clearBST(root);
    }

    void start() {
        welcomeMsg();
        while (true) {
            for (int i = 0; i < 2; ++i) {
                cout << players[i]->getName() << ": " << getTurnText() << " Hit Enter to roll dice: ";
                getchar();
                cout << "\nRolling dice..." << endl;
                int diceValue = getDiceValue();
                cout << players[i]->getName() << " moving...." << endl;
                movePlayer(players[i], diceValue);
                if (checkWin(players[i])) {
                    cout << players[i]->getName() << " has won the game. Congratulations!" << endl;
                    return;
                }
            }
        }
    }

private:
    void welcomeMsg() {
        cout << "\nWelcome to Snakes and Ladders.\n\nRules:\n";
        cout << "1. Initially both the players are at starting position i.e. 0.\n";
        cout << "2. Take turns to roll the dice.\n";
        cout << "3. Move forward the number of spaces shown on the dice.\n";
        cout << "4. If you land at the bottom of a ladder, you can move up to the top of the ladder.\n";
        cout << "5. If you land on the head of a snake, you must slide down to the bottom of the snake.\n";
        cout << "6. The first player to get to the FINAL position is the winner.\n";
        cout << "7. Hit enter to roll the dice.\n\n";
    }

    string getTurnText() {
        string turnText[] = {
            "Your turn.",
            "Go.",
            "Please proceed.",
            "Let's win this.",
            "Are you ready?",
            ""
        };
        return turnText[rand() % 5];
    }

    int getDiceValue() {
        
        srand(time(NULL));
        return rand() % DICE_FACE + 1;
    }

    void initializeSnakes() {
        snakes = {
            {8, 4}, {18, 1}, {26, 10}, {39, 5}, {51, 6}, {54, 36}, {56, 1},
            {60, 23}, {75, 28}, {83, 45}, {85, 59}, {90, 48}, {92, 25}, {97, 87}, {99, 63}
        };
    }

    void initializeLadders() {
        ladders = {
            {3, 20}, {6, 14}, {11, 28}, {15, 34}, {17, 74}, {22, 37}, {38, 59},
            {49, 67}, {57, 76}, {61, 78}, {73, 86}, {81, 98}, {88, 91}
        };
    }

    void buildBST() {
        for (const auto& snake : snakes) {
            root = insertNode(root, snake.first, snake.second);
        }

        for (const auto& ladder : ladders) {
            root = insertNode(root, ladder.first, ladder.second);
        }
    }

    Node* insertNode(Node* root, int key, int value) {
        if (root == NULL) {
            return new Node(key, value);
        }

        if (key < root->key) {
            root->left = insertNode(root->left, key, value);
        } else if (key > root->key) {
            root->right = insertNode(root->right, key, value);
        }

        return root;
    }

    void movePlayer(Player* player, int diceValue) {
        int oldPosition = player->getCurrentPosition();
        int newPosition = oldPosition + diceValue;
        cout << "It's a " << diceValue << endl;
        cout << player->getName() << " moved from " << oldPosition << " to " << newPosition << endl;

        int finalPosition = searchBST(root, newPosition);
        if (finalPosition != -1) {
            if (finalPosition < newPosition) {
                gotSnakeBite(newPosition, finalPosition, player->getName());
            } else {
                gotLadderJump(newPosition, finalPosition, player->getName());
            }
            player->move(finalPosition - oldPosition);
        } else {
            player->move(diceValue);
        }
    }

    int searchBST(Node* root, int key) {
        if (root == NULL || root->key == key) {
            return (root == NULL) ? -1 : root->value;
        }

        if (key < root->key) {
            return searchBST(root->left, key);
        } else {
            return searchBST(root->right, key);
        }
    }

    void gotSnakeBite(int oldPosition, int newPosition, const string& playerName) {
        string messages[] = {
            "boohoo",
            "bummer",
            "snake bite",
            "oh no",
            "dang"
        };
        cout << messages[rand() % 5] << " ~~~~~~~~>\n";
        cout << playerName << " got a snake bite. Down from " << oldPosition << " to " << newPosition << endl;
    }

    void gotLadderJump(int oldPosition, int newPosition, const string& playerName) {
        string messages[] = {
            "woohoo",
            "woww",
            "nailed it",
            "woah",
            "yaayyy"
        };
        cout << messages[rand() % 5] << " ########\n";
        cout << playerName << " climbed the ladder from " << oldPosition << " to " << newPosition << endl;
    }

    bool checkWin(Player* player) {
        return player->getCurrentPosition() >= MAX_VAL;
    }

    void clearBST(Node* root) {
        if (root == NULL) return;
        clearBST(root->left);
        clearBST(root->right);
        delete root;
    }
};

int main() {
    string player1Name, player2Name;
    cout << "Please enter a valid name for the first player: ";
    getline(cin, player1Name);
    cout << "Please enter a valid name for the second player: ";
    getline(cin, player2Name);

    SnakesAndLadders game(player1Name, player2Name);
    game.start();

    return 0;
}
