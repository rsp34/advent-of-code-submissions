#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ifstream file("C:/Users/User/advent-od-code/c++/day-1/example.txt");

    string line;
    int turns = 0;
    enum Direction
    {
        Right = 'R',
        Left = 'L'
    };
    int sign = 1;
    int count = 0;
    int position = 50;
    int start_position;

    if (file.is_open())
    {
        while (getline(file, line))
        {
            Direction direction = (Direction)line[0];
            turns = stoi(line.substr(1));
            if (direction == Direction::Left)
            {
                sign = -1;
            }
            else
            {
                sign = 1;
            }
            start_position = position;
            position += sign * turns;
            if (position <= 0 || position >= 100)
            {
                position = ((position % 100) + 100) % 100;
                count += 1;
            };
            count += 1 + (turns - 1) / 100;
            cout << "Input: " << line << ", Start Position: " << (start_position) << ", End Position: " << position << ", Count: " << count << "\n";
        }
    }

    file.close();

    cout << "Total Count: " << count << endl;
};