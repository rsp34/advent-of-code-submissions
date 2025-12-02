#include <fstream>
#include <iostream>
#include <string>

int main()
{
    std::ifstream file("C:/Users/User/advent-od-code/c++/day-1/input.txt");

    std::string line;
    int turns = 0;
    enum Direction
    {
        Right = 'R',
        Left = 'L'
    };
    int count = 0;
    int position = 50;

    if (file.is_open())
    {
        while (getline(file, line))
        {
            Direction direction = static_cast<Direction>(line[0]);
            turns = std::stoi(line.substr(1));
            if (direction == Direction::Left)
            {
                position -= turns;
            }
            else
            {
                position += turns;
            }
            position = position % 100;
            if (position == 0)
            {
                count += 1;
            }

        }
    }

    file.close();

    std::cout << count << std::endl;
}