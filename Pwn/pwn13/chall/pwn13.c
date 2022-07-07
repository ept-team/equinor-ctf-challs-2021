#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>


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

void banner() {
    puts(" _______   __       __  __    __    __    ______  ");
    puts("|       \\ |  \\  _  |  \\|  \\  |  \\ _/  \\  /      \\ ");
    puts("| $$$$$$$\\| $$ / \\ | $$| $$\\ | $$|   $$ |  $$$$$$\\");
    puts("| $$__/ $$| $$/  $\\| $$| $$$\\| $$ \\$$$$  \\$$__| $$");
    puts("| $$    $$| $$  $$$\\ $$| $$$$\\ $$  | $$   |     $$");
    puts("| $$$$$$$ | $$ $$\\$$\\$$| $$\\$$ $$  | $$  __\\$$$$$\\");
    puts("| $$      | $$$$  \\$$$$| $$ \\$$$$ _| $$_|  \\__| $$");
    puts("| $$      | $$$    \\$$$| $$  \\$$$|   $$ \\$$    $$");
    puts(" \\$$       \\$$      \\$$ \\$$   \\$$ \\$$$$$$ \\$$$$$$ ");
    puts("\n Welcome to PWN13, the awesome encryption engine!");
    puts("At this stage we dont accept strings longer than 100 characters, so play nice :)");
}

void ignore_me_init_signal() {
    signal(SIGALRM, kill_on_timeout);
    alarm(60);
}

    void rot13( char * str ) 
    {
        int i = 0;
        for( i = 0; str[ i ] != '\0' ; i++ ){
            if (( *( str + i ) >= 'a' && *( str + i ) < 'n')|| ( *( str + i ) >= 'a' && *( str + i ) < 'n')) 
                *( str + i ) += 13;       
            else if(( *( str + i ) >= 'n' && *( str + i ) <= 'z') || ( *( str + i ) >= 'N' && *( str + i ) <= 'Z')) 
                *( str + i ) -= 13;
        }
    }


int main() {
    int idx = 0;
    ignore_me_init_buffering();
    ignore_me_init_signal();
    banner();
    char c;
    char text[100];
    printf("Enter text: ");
    while ( !feof(stdin) ) {
        c = fgetc(stdin);
        if ( c == '\n' )
            break;
        text[idx] = c;
        idx++;
  }

    rot13(text);
    printf("Result: ");
    puts(text);
    return 0;
}