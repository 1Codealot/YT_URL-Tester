#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

const char Characters[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_";

char getRandomChar() {
    int index = rand() % (sizeof(Characters) - 1);
    return Characters[index];
}

char* makeURL() {
    static char URL[] = "https://www.youtube.com/watch?v=###########";

    for (int i = 32; i < 43; ++i) {
        URL[i] = getRandomChar();
    }

    return URL;
}

int main() {
    srand((unsigned)time(NULL));

    for(int n; n <= 100; n++){
        char* URL = makeURL();
        printf("%s\n", URL);
}

    return 0;
}
