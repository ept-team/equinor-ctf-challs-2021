#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>
#include <signal.h>
#include <unistd.h>
//TODO maybe have function pointers in the struct?
char *feedbackStr = "Dear %s,\n"
"Thank you for using Shit as a Service! We’d love to hear what you think of our service. Your feedback will help us determine what features to add and how we can make the shit better for you.\n"
"If you have 5 hours, please write us a short feedback. [When you complete it, your name will be entered in a draw to win one of 20 shits vouchers.]\n\n"
"Thanks again!\n\n"
"- nordbo\n\nName: ";
char *feedbackStr2 = "Feedback: ";
char *feedbackStr3 = "Thank you for the feedback %s!\n We will use or shit AI to analyze it right away!\n\n";
char *guestMenu = "\n"
      "1. Login\n"
      "2. Send feedback\n"
      "\n"
      "Please enter an operation number: \n"
      "> ";

char *userMenu = "\n"
      "1. Logout\n"
      "2. Send feedback\n"
      "\n"
      "Please enter an operation number: \n"
      "> ";

typedef enum {Guest, FreeTier, Premium = 0x13371337} Access;

typedef struct {
    char username[50];
    Access access;
   char passwordHash[33];
   
} Account;

Account * acc;

Account accounts[11]  = {
    {"Viipz",       FreeTier, "\x82\x37\x04\x86\x03\xa7\xf3\x0f\x88\x94\x84\xcc\xc2\x98\x3d\xb7\xef\x2f\x19\xed\x0b\x64\x9c\x27\x4e\xb1\xa5\x26\x73\xc3\xb0\x9e"},
    {"LOLASL",      FreeTier, "\xb8\xa4\x7e\x47\x3f\x75\xa1\x1f\xb0\xb8\x11\xfe\xc1\xcd\x12\x16\xaf\x88\x9b\x63\xe7\x99\xd7\xde\x2d\x8e\x3d\x47\xaf\xff\x90\x05"},
    {"Sweeet",      FreeTier, "\x19\x13\x8f\xe8\x40\x65\xd5\x04\x19\x74\x8e\x9f\xf8\x8a\xe1\x99\xee\xa0\xf5\x4a\x59\x84\x32\x93\x04\x9c\xbb\x30\x14\xfe\x28\x7a"},
    {"mockingjay",  FreeTier, "\xdd\x9f\x4c\xb0\x67\x7b\x63\x10\xef\x28\xd3\x8e\x1f\x9a\x09\x11\x61\x25\xcd\x4c\x46\x7a\x9a\xf5\x2a\x3e\xa7\x08\x96\x5d\x82\xe8"},
    {"zledge",      FreeTier, "\xea\x60\x42\x82\x52\x40\x47\x75\xbe\xfc\x6f\x8e\x11\xad\xd7\xb1\xf8\x9d\x37\x40\x66\x48\x11\xc1\x5d\x83\x20\x58\x50\xe2\x6b\x04"},
    {"kekburger",   Premium, "\x6c\x14\xa7\x10\xe7\x9f\xb6\xfe\xbe\x18\x28\xec\xca\x3d\x1a\xf4\xf2\x04\xd0\x52\x92\x81\x56\x12\xd8\xb7\x36\xba\xfe\xaf\xe1\x72"},
    {"vcpo",        FreeTier, "\x87\x5b\xae\x75\x1d\x6f\x87\x0f\x1b\x36\xc7\xd3\x03\xec\x5a\x6a\x54\xe6\x87\xcd\x92\x34\xa5\x40\x78\x38\x79\xda\x3e\xbf\x60\x4b"},
    {"rvino",       FreeTier, "\xb1\x75\xdc\xf1\x90\x92\xd8\xae\x07\x4e\x7c\x2d\xfa\x92\xae\x55\xe1\xa9\x23\x17\x0d\x0f\x05\x46\x48\x7e\xa1\xbe\x62\xd3\xab\x29"},
    {"iLoop",       FreeTier, "\x05\x0e\x80\x6d\x81\xd6\x59\x96\x21\x30\xdf\x46\xd1\xec\x9a\xf2\x8a\x97\x6e\x9c\xb4\x29\x5b\x8c\xb7\x68\xde\xa0\x12\xdd\xfe\xbd"},
    {"null",        FreeTier, "\x14\x93\xd0\x17\xe6\x70\x7e\xf7\x09\xff\xd9\x68\x39\x89\x9f\x2a\xd2\x20\xa9\x9c\x10\x53\x92\x5c\x74\x02\x2a\x6b\x1f\x50\xa3\xab"},
    {"starsiv",     FreeTier, "\x46\x72\x2c\x3d\x90\x3d\x81\xf0\xc7\x9a\x1d\x5d\x47\xfb\x51\xa9\xdc\x07\xae\x85\xd5\x2b\xfd\x54\x06\xf1\x57\xbc\x5d\x0e\x2c\x9e"},
     };

void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
    if (sig == SIGALRM) {
        printf("[!] Anti DoS Signal. Patch me out for testing.");
        _exit(0);
    }
}

void ignore_me_init_signal() {
    signal(SIGALRM, kill_on_timeout);
    alarm(60);
}

void banner() {
    FILE *fptr;
    fptr = fopen("art.txt", "r");
    if (fptr == NULL)
    {
        printf("Cannot open file \n");
        exit(0);
    }
    char c;
    c = fgetc(fptr);
    while (c != EOF)
    {
        printf ("%c", c);
        c = fgetc(fptr);
    }
  
    fclose(fptr);
}

void feedback(char* user) {

    printf(feedbackStr, user);
    char s [256];
    fgets(s, 256, stdin);
    char* name = strdup(s);
    name[strcspn(name, "\n")] = 0;
    printf(feedbackStr2, name);
    fgets(s, 256, stdin);
    char* feedbackz = strdup(s);
    printf(feedbackStr3, name);
    
}

int getChoice() {
    int i;
    char inp [4];
    fgets(inp, 4, stdin);
    inp[strcspn(inp, "\n")] = 0;
    return atoi(inp);
}


Account* login(){
    char inputUserName[20];
    char password[50];

        printf("Username: ");
        fgets(inputUserName, 20, stdin);
        inputUserName[strcspn(inputUserName, "\n")] = 0;
        printf("Password: ");
        fgets(password, 50, stdin);
        password[strcspn(password, "\n")] = 0;
        fflush(stdin);
        char *hash = SHA256(password, strlen(password), 0);
        
        for(int i = 0; i < sizeof(accounts) / sizeof( Account); i++) {
            if(strcmp(accounts[i].username,inputUserName) == 0 && memcmp(accounts[i].passwordHash,hash, 32) == 0) {
                return &accounts[i];
            }
        }
        puts("Login failed!");
        return NULL;

        
 
}

Account*  GuestMenu() {
    Account *a;
     printf("%s", guestMenu);
    int inputChoice = getChoice();
    switch(inputChoice) {
        case 1:
            a =  login();
            if (a != NULL) {
                puts("Login successfull!");
            }
            return a;
            break;
        case 2:
            feedback("Guest");
            break;
        default:
            puts("invalid!");
    }
}

void logout() {
    acc->access = Guest;
    free(acc);
    puts("you've successfully logged out!");

}

void UserMenu() {
     printf("%s", userMenu);
    int inputChoice = getChoice();
    switch(inputChoice) {
        case 1:
            return logout();
            break;
        case 2:
            feedback(acc->username);
            break;
        default:
            puts("invalid!");

    }
}
void printFlag()  {
    FILE *fp;
    char buff[255];
    char ch;
    fp = fopen("/opt/flag", "r");
    while((ch = fgetc(fp)) != EOF)
        printf("%c", ch);
    fclose(fp);
}
int main() {
    ignore_me_init_buffering();
    ignore_me_init_signal();
    banner();
    Account *temp;
    acc = malloc(sizeof(Account));
    acc->access = Guest;
    while(1) {
        switch(acc->access) {
            case Guest:
                    temp = GuestMenu();
                if (temp != NULL) {
                    memcpy(acc, temp, sizeof(Account));
                }
                break;
            case FreeTier:
                UserMenu();
                break;
            case Premium:
                printFlag();
                exit(1);
            default:
                puts("Error!");
                exit(1337);
        }
    }
    return 0;
}





