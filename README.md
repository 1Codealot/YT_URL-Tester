# YT_URL-Tester
A script in C and python for creating YouTube URLs and testing if it exists. Too much of this was written by ChatGPT.

# Building and Running
To build the `.c` file you must build it to `.so`. You can use this command: `g++ -O3 -Wall -shared -std=c++11 -fPIC -o URL_Creator.so URL_Creator.cpp` Then just run the `Tester.py` file. To compile the python code to `.exe` use this command: `pyinstaller --onefile --add-binary "URL_Creator.so;." Tester.py`
