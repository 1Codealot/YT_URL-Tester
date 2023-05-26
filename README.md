# YT_URL-Tester
A script in C and python for creating YouTube URLs and testing if it exists. Too much of this was written by ChatGPT.

# Building and Running
To run the `.exe` file, it must be in the same folder as the `URL_Creator.so` file. However if you use a shortcut, it will work.
To build the `.c` file you must build it to `.so`. You can use this command: `g++ -O3 -Wall -shared -std=c++11 -fPIC -o URL_Creator.so URL_Creator.cpp` Then jus run the `Tester.py` file.
