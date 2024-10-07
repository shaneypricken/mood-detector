// aaaaa.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Shane Pricken
// Switch statement lab
//10/7/2024
// Extra: weird feelings

#include <iostream>
using namespace std;

int main()
{
    int ans;
    cout << "What emotion are you feeling today?!?!?!?!?!?!?!?!?!?!!??!?!?!?!" << endl;

    cout << "1. Obnoxiousness" << endl;
    cout << "2. Adronitis" << endl;
    cout << "3. Jouska" << endl;
    cout << "4. Enouement" << endl;
    cout << "5. Liberosis" << endl;
    cin >> ans;

    switch (ans) {
    case 1: cout << "Ah, the good ol' obnoxiousness. You must be feeling pretty unpleasent and angry today. Hope it gets better :)";
        break;
    case 2: cout << "I mean who hasn't felt adronitis before? I always feel frustrated with the amount of time required to be truly familliar with something.";
        break;
    case 3: cout << "So you are basically crazy because you always have hypothetical conersations that you compulsively play out in your head. weirdo.";
        break;
    case 4: cout << "You must love the future because you are happy with arriving in the future, seeing how things turn out, and not being able to tell your past self.";
        break;
    case 5: cout << "Not a care in the world. You don't even care about whats going to happen, or what already happened. Must be relaxing.";
        break;
    default: cout << "Thats not a valid number silly, and its okay! Not everyone knows how numbers work.";
        break;
    }
}



