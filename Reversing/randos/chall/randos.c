#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define SEC_LENGTH 12
#define NUMBER_OF_STRING 20
#define MAX_STRING_SIZE 150
#define FREE_QUOTES 3
int secretKey[SEC_LENGTH] = {0x6c,0x6f,0x6c,0x20,0x69,0x74,0x73,0x20,0x72,0x61,0x6e,0x64};
int registrationKey[SEC_LENGTH];
int validRegistrationCode = 0;

void init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

char *menuString = "\n"
      "Select option:\n"
      "1. Get quote\n"
      "2. Exit\n"
      " \n> ";

char quotes[NUMBER_OF_STRING][MAX_STRING_SIZE] =
{ "Rome did not create a great empire by having meetings, they did it by killing all people who opposed them.",
"If you can stay calm, while all around you is chaos…then you probably haven’t completely understood the seriousness of the situation.",
"Doing a job RIGHT the first time gets the job done. Doing the job WRONG fourteen times gives you job security.",
"Eagles may soar, but weasels don’t get sucked into jet engines.",
"Artificial Intelligence is no match for Natural Stupidity",
"A person who smiles in the face of adversity…probably has a scapegoat.",
"Plagiarism saves time.",
"If at first you don’t succeed, try management.",
"Never put off until tomorrow what you can avoid altogether.",
"TEAMWORK…means never having to take all the blame yourself.",
"The beatings will continue until morale improves.",
"Never underestimate the power of very stupid people in large groups.",
"We waste time, so you don’t have to.",
"Hang in there, retirement is only fifty years away!",
"Go the extra mile. It makes your boss look like an incompetent slacker",
"A snooze button is a poor substitute for no alarm clock at all.",
"When the going gets tough, the tough take a coffee break.",
"INDECISION is the key to FLEXIBILITY.",
"Succeed in spite of management.",
"Aim Low, Reach Your Goals, Avoid Disappointment."
};

//registrationKey[i] = registrationKey[i] ^ rand();
void readVerificationCode() {    
    puts("Please enter registration key: ");
    for (int i = 0; i < SEC_LENGTH; i++) {
        scanf("%d", &registrationKey[i]);
    }
}

char getChoice() {
    char inputChoice;
    do {
    inputChoice = getchar();
    } while ( inputChoice == 10 && inputChoice == -1 );
    char non;
    do {
        non = getchar();
    }
    while ( non != 10 && non != -1 );
    return inputChoice;
}

void updateSecret() {
    int r = rand() & 0xc0de;
    for (int i = 0; i < r; i++) {
        rand();
    }
    for (int i = 0; i < SEC_LENGTH; i++) {
        secretKey[i] = (secretKey[i] ^ rand()) << i;
    }
}

int validateVerificationCode() {
     for (int i = 0; i < SEC_LENGTH; i++) {
        if(registrationKey[i] != secretKey[i]) {
            return 0;
        }
    }
}

void success()  {
    puts("Well done, here is your flag: "); 
    FILE *fp;
    char buff[255];
    char ch;
    fp = fopen("/opt/flag", "r");
    while((ch = fgetc(fp)) != EOF)
        printf("%c", ch);
    puts("");
    fclose(fp);
}

void setupSystem() {
    time_t tim = time(NULL);
    srand(tim);
    //printf("%d\n", tim);
}

void menu() {
    printf("%s",menuString);
}

void validateRegistrationKey() {
    readVerificationCode();
    updateSecret();
    if(validateVerificationCode()) {
        validRegistrationCode = 1;
    }
    else {
        puts("Invalid registration key, exiting.");
        exit(1);
    }
}

void printQuote(int *numQuotes) {
    if ((*numQuotes) < FREE_QUOTES) {
        int a = rand();
        printf("%s", quotes[a % NUMBER_OF_STRING]);
        (*numQuotes)++;
    }
    else if (!validRegistrationCode) {
        puts("No more free quotes. Please enter a registration key to continue using this great service.");
        validateRegistrationKey();
        if (validRegistrationCode) {
            success();
        }
    }
    else {
        success();
    }
}

int main() {
    int numQuotes =0;
    char c;
    init_buffering();
    setupSystem();
    while(1) {
        menu();
        c = getChoice();
        switch(c) {
            case '1':
            printQuote(&numQuotes);
            break;
            case '2':
                exit(1);
            
        }
    }
    
    
   
    return 0;
}