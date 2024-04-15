#include <iostream>
#include <algorithm>
using namespace std;

class node {
public:
    string key, value;
    node *left = nullptr, *right = nullptr;
    int height = 1;
    node(string k = "", string v = "") : key(k), value(v) {}
};

class AVL {
    node* root = nullptr;

    int height(node* n) { return n ? n->height : 0; }
    int balanceFactor(node* n) { return n ? height(n->left) - height(n->right) : 0; }

    node* rightRotate(node* y) {
        node* x = y->left;
        y->left = x->right; x->right = y;
        y->height = 1 + max(height(y->left), height(y->right));
        x->height = 1 + max(height(x->left), height(x->right));
        return x;
    }

    node* leftRotate(node* x) {
        node* y = x->right;
        x->right = y->left; y->left = x;
        x->height = 1 + max(height(x->left), height(x->right));
        y->height = 1 + max(height(y->left), height(y->right));
        return y;
    }

    node* insert(node* temp, string k, string v) {
        if (!temp) return new node(k, v);
        if (k < temp->key) temp->left = insert(temp->left, k, v);
        else if (k > temp->key) temp->right = insert(temp->right, k, v);
        temp->height = 1 + max(height(temp->left), height(temp->right));
        int bf = balanceFactor(temp);
        if (bf > 1 && k < temp->left->key) return rightRotate(temp);
        if (bf < -1 && k > temp->right->key) return leftRotate(temp);
        if (bf > 1 && k > temp->left->key) { temp->left = leftRotate(temp->left); return rightRotate(temp); }
        if (bf < -1 && k < temp->right->key) { temp->right = rightRotate(temp->right); return leftRotate(temp); }
        return temp;
    }

    void traverse(node* n, bool ascending) {
        if (n) {
            traverse(ascending ? n->left : n->right, ascending);
            cout << n->key << ":" << n->value << endl;
            traverse(ascending ? n->right : n->left, ascending);
        }
    }

public:
    bool modify(string k, string v, bool insert) {
        node** temp = &root;
        while (*temp) {
            if ((*temp)->key == k) { if (insert) return false; (*temp)->value = v; return true; }
            temp = k < (*temp)->key ? &((*temp)->left) : &((*temp)->right);
        }
        *temp = new node(k, v);
        return true;
    }

    bool remove(string k) {
        node** temp = &root;
        while (*temp) {
            if ((*temp)->key == k) {
                node* t = *temp;
                if (!t->left || !t->right) {
                    *temp = t->left ? t->left : t->right;
                    delete t;
                } else {
                    node** minRight = &t->right;
                    while ((*minRight)->left) minRight = &((*minRight)->left);
                    swap(t->key, (*minRight)->key);
                    swap(t->value, (*minRight)->value);
                    temp = minRight;
                }
                return true;
            }
            temp = k < (*temp)->key ? &((*temp)->left) : &((*temp)->right);
        }
        return false;
    }

    void display(bool ascending) {
        if (!root) cout << "Tree is Empty" << endl;
        else {
            cout << (ascending ? "Ascending" : "Descending") << " Traversal is" << endl;
            traverse(root, ascending);
        }
    }
};

int main() {
    AVL tree;
    int ch;
    string k, v;
    do {
        cout << endl << "--: MENU :--\n1. Insert\n2. Search\n3. Update\n4. Delete\n5. Display Descending\n6. Display Ascending\n0. Exit\nENTER YOUR CHOICE:";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Enter key to insert:"; cin >> k; cout << "Enter value:"; cin >> v; cout << (tree.modify(k, v, true) ? "Element Inserted Successfully" : "Element Already Present") << endl; break;
            case 2: cout << "Enter key to search:"; cin >> k; cout << (tree.modify(k, "", false) ? "Value is " + tree.modify(k, "", false) : "Element Not Found") << endl; break;
            case 3: cout << "Enter key to Update:"; cin >> k; cout << "Enter new value:"; cin >> v; cout << (tree.modify(k, v, false) ? "Element Updated Successfully" : "Element Not Present") << endl; break;
            case 4: cout << "Enter key to Delete:"; cin >> k; cout << (tree.remove(k) ? "Element Deleted Successfully" : "Element Not Present") << endl; break;
            case 5: tree.display(false); break;
            case 6: tree.display(true); break;
            case 0: cout << "Thank You!" << endl; break;
            default: cout << "Please Enter a valid choice" << endl; break;
        }
    } while (ch != 0);
    return 0;
}
