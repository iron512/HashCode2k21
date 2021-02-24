#include <iostream>
#include <cstring>
#include <cstdlib>
#include <fstream>

#define CCYN "\033[96m"
#define CGRN "\033[92m"
#define CRED "\033[91m"
#define CRST "\033[0m"

using namespace std;

int solution(string filename) {
	fstream reader("../inputs/" + filename, ios::in);
	string tmp;
	getline(reader,tmp);

	cout << tmp << endl;
	reader.close();
	return 0;
}

int main(int argc, char const *argv[])
{	
	fstream anchor("../files.txt", ios::in);
	string row;
	int length = 0;

	string* inputs =  new string[argc];

	cout << CCYN << "\tC++" << CRST << endl << endl;
	cout << "Loading inputs from files.txt:\n\n";
	while (getline(anchor, row)) {
		cout << "\t- " << row << "\n";
		inputs[length] = row;
		length++;
	}
	cout << endl;

	if (argc-1 != length) {
		cout << "Wrong argument count" << endl;
		exit(1);
	}

	for (int i = 1; i < argc; ++i) {
		if (atoi(argv[i]) == 1) {
			cout << "(1) Running algs on: " << CGRN << inputs[i-1] << CRST << endl;
			solution(inputs[i-1]);
		}
		else {
			cout <<"(0) Not running algs on: " << CRED << inputs[i-1] << CRST << endl;
		}
	}

	cout << endl;
	return 0;
}