#include <stdio.h>
#include <string.h>

char flag[] = {0x56,0x67,0x47,0x4c,0x6b,0x07,0x61,0x68,0x67,0x58,0x4c,0x43,0x76,0x5f,0x4c,0x5a,0x23,0x07,0x23,0x07,0x23,0x07,0x23,0x07,0x7d,0x16,0x6e};

int checkFlag(char* input) {
    int len = strlen(flag);
    for (int i = 0; i < len; i++) {
        if(i % 2 == 1 && (input[i] ^ 0x37) != flag[i]) {
            return 0;
        }
        else if(i % 2 == 0 && (input[i] ^ 0x13) != flag[i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    
    char input[50];
    printf("%s","Enter the flag: ");
    fgets(input,50, stdin);
    input[strcspn(input, "\n")] = 0;
    if(checkFlag(input)) {
        puts("Well done, that is correct!");
    }
    else {
        puts("Sorry, flag is not correct :/");
    }
    return 0;
}

//  EPT{x0r_to_teh_m00000000n!}