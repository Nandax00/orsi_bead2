#include <fstream>
#include <thread>
#include <iostream>
#include <string>
#include <tuple>

class Character
{
	std::string _level;
	std::string _gender;
	std::string _race;
	std::string _class;

public:
	std::string getLevel() const {return _level;}
	std::string getGender() const {return _gender;}
	std::string getRace() const {return _race;}
	std::string getClass() const {return _class;}

	Character& operator=(std::array<std::string, 4> attrib)
	{
		_level = attrib[0];
		_gender = attrib[1];
		_race = attrib[2];
		_class = attrib[3];
		return *this;
	}

	bool operator==(const Character& c) const
	{
		return this->_level == c._level && this->_gender == c._gender && this->_race == c._race && this->_class == c._class;
	}
};

std::ostream& operator<<(std::ostream& os, const Character& c)
{
	    return os << "Level: " + c.getLevel() << std::endl << "Class: " + c.getClass() << std::endl << "Race: " + c.getRace() << std::endl << "Gender: " + c.getGender() << std::endl;
}

int main()
{
	std::ifstream input("input.txt");
	int M;
	input >> M;
	Character players[M];

	std::string buffer;
	//reads until endline
	std::getline(input, buffer);

	std::array<std::string, 4> attributes;
	for (int i = 0; i < M; ++i)
	{
		//Order of a line: <class,race,level,gender,misc.>.
		//The order of declarations in Character is kept, because
		//that is the order of the output (<level,class,race,gender>).
		//The miscellaneous attributes are dumped into the buffer.
		std::getline(input, attributes[3], ';');
		std::getline(input, attributes[2], ';');
		std::getline(input, attributes[0], ';');
		std::getline(input, attributes[1], ';');
		players[i] = attributes;
		std::getline(input, buffer);
		std::cout << players[i];
	}

	//DEBUG
	std::cout << (players[0] == players[1]);

	return 0;
}