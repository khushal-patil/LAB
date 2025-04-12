#include <iostream>
#include <string>
using namespace std;
// base class publication
class publication
{
public:
    string title;
    float prices;

    publication()
    {
        title = "";
        prices = 0.0;
    }
    void get_data()
    {
        cout << "Enter Title :";
        cin>>title;
        cout << "Enter Price : ";
        cin >> prices;
    }
    void put_data()
    {
        cout << " Title :" << title<<"\n";
        cout << " Price :" << prices<<"\n";
    }
};
class book : public publication
{
private:
    float pages;
    int temp;

public:
    book(){
        pages = 0;
    }
    void get_data(){
        publication::get_data();
        cout << "Enter Page Count: ";
        cin >> pages;
        temp = int(pages);
    }
    void put_data(){
        try{
            if (pages != temp || pages < 0){
                throw pages;
            }else{
                publication::put_data();
                cout << " Pages Are :" << pages<<endl;
            }
        }catch (...){
            publication::title="-";
            publication::prices=0.0;
            pages = 0;
            cout << " Name :" << publication::title<<endl;
            cout << " Price :" << publication::prices<<endl;
            cout << " Pages Are :" << pages<<endl;
        }
        
    }
};
class tape : public publication
{
private:
    float playtime;
    int temp;

public:
    tape(){
        playtime = 0.0;
    }
    void get_data(){
        publication::get_data();
        cout << "Enter Play Time Of Cassette: ";
        cin >> playtime;
        temp = int(playtime);
    }
    void put_data(){
        
        try
        {
            if (playtime < 0.0|| playtime == temp){
                throw playtime;
            }else{
                publication::put_data();
                cout << " Playtime is : " << playtime<<" Minutes"<<endl;
            }
        }
        catch (float r)
        {
            publication::title="-";
            publication::prices=0.0;
            playtime = 0.0;
            cout << " Name :" << publication::title<<endl;
            cout << " Price :" << publication::prices<<endl;
            cout << " Playtime is : " << playtime<<" Minutes"<<endl;
        }
        
    }
};
int main()
{
    book b; 
    tape t;
    int choice = 0;
   
    do
    {
        cout << "\n 1. Add book ";
        cout << "\n 2. Add tape: ";
        cout << "\n 3. Exit:";
        cout << "\nEnter Choice : ";
        cin >> choice;
        switch (choice)
        {
        case 1:
        {
           
            cout << "Add Book: \n";
            b.get_data();
            cout<<"\nBook Details: "<<endl;
            b.put_data();
            break;
        }
        case 2:
        {
           
            cout << "Add Tape: \n";
            t.get_data();
            cout << "\n Tape Detials: "<<endl;
            t.put_data();
        
            break;
        }
        case 3:
        {
            cout << "Thank You..."<<endl;
            exit(0);
        }
        default:
        {
            cout << "\n Invalid";
        }
        }
    } while (choice != 5);
    return 0;
}