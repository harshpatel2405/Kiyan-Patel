#include <iostream>
using namespace std;
class Pizza
{
protected:
    int pizzaID;
    string name;
    string size;
};
class VegPizza : public Pizza
{
protected:
    bool isVeg;
    string vegType;

public:
    void scanData()
    {
        cout << "\nEnter PizzaId : ";
        cin >> pizzaID;
        cin.ignore();

        cout << "\nEnter Pizza Name : ";
        getline(cin, name);
        cout << "\nEnter Pizza Size : ";
        getline(cin, size);
        cout << "\nIsVeg? :  ";
        cin >> isVeg;
        cout << "\nEnter VegType : ";
        cin >> vegType;
    }
    void dispData()
    {
        cout << "\n"
             << pizzaID << "\t" << name << "\t" << size << "\t" << isVeg << "\t" << vegType;
    }
};
class cheesePizza : public Pizza
{
protected:
    bool isExtraCheese;
    int cheeselayers;

public:
    void scanData()
    {
        cout << "\nEnter PizzaId : ";
        cin >> pizzaID;
        cin.ignore();
        
        cout << "\nEnter Pizza Name : ";
        getline(cin, name);
        cin.ignore();
        cout << "\nEnter Pizza Size : ";
        getline(cin, size);
        cout << "\nIsExtraCheese? :  ";
        cin >> isExtraCheese;
        cin.ignore();
        cout << "\nCheese Layers : ";
        cin >> cheeselayers;
    }
    void dispData()
    {
        cout << "\n"
             << pizzaID << "\t" << name << "\t" << size << "\t" << isExtraCheese << "\t" << cheeselayers;
    }
};
int main()
{
    VegPizza vp;
    cheesePizza cp;
    vp.scanData();
    vp.dispData();
    cp.scanData();
    cp.dispData();
    return 0;
}