#include <stdio.h>
#include <string.h>

char flag[] = "EPT{strings_are_great!}";

int checkFlag(char* input) {
    int len = strlen(flag);
    if (!strcmp(flag, input)){
        return 1;
    }
    return 0;
}

int main() {
    char input[50];
    printf("%s","Magical programs can hide magical strings, can you find a flag?\n");
    printf("%s","Enter flag to validate: ");
    fgets(input,50, stdin);
    input[strcspn(input, "\n")] = 0;
    if(checkFlag(input)) {
        puts("That is correct, sir!");
    }
    else {
        puts("nope :/");
    }
    return 0;
}

