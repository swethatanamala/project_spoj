#include <iostream>
#include <string>

int main()
{
    while (true) {
        std::string line;
        std::getline(std::cin, line);
        int input = stoi(line);
        if (input == 0) {
            break;
        }
        else {
            int result = 0;
            for (int i = 1; i <= input; i++){
                result = result + i * i;
            }
            std::cout << result << "\n";
        }
    }
}