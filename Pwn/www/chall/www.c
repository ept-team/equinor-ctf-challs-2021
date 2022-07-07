#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <stdbool.h>

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
    puts("           .---.           .---.           .---. ");
    puts("          /. ./|          /. ./|          /. ./| ");
    puts("      .--'.  ' ;      .--'.  ' ;      .--'.  ' ; ");
    puts("     /__./ \\ : |     /__./ \\ : |     /__./ \\ : | ");
    puts(" .--'.  '   \\' . .--'.  '   \\' . .--'.  '   \\' . ");
    puts("/___/ \\ |    ' '/___/ \\ |    ' '/___/ \\ |    ' ' ");
    puts(";   \\  \\;      :;   \\  \\;      :;   \\  \\;      : ");
    puts(" \\   ;  `      | \\   ;  `      | \\   ;  `      | ");
    puts("  .   \\    .\\  ;  .   \\    .\\  ;  .   \\    .\\  ; ");
    puts("   \\   \\   ' \\ |   \\   \\   ' \\ |   \\   \\   ' \\ | ");
    puts("    :   '  |--\"     :   '  |--\"     :   '  |--\"  ");
    puts("     \\   \\ ;         \\   \\ ;         \\   \\ ;     ");
    puts("      '---\"           '---\"           '---\"      ");
    puts("Welcome to WriteWhatWhere!\n\n ");
}

void * addr = banner;
void ** addr2 = &addr;

int main (void) {
    bool done = false;
    long * lol;
    ignore_me_init_buffering();
    ignore_me_init_signal();
    banner();
    char buffer[20];
    while(!done) {
        
        printf ("Where? for example [%p]\n> ", (*addr2));
        
        fgets(buffer, 20, stdin);
        
        long address = (long)strtol(buffer, NULL, 0);
        //printf("address is: 0x%lx \n", address);
        printf ("What?  for example [0xdeadc0de]\n > ");
        fgets(buffer, 20, stdin);
        long value = (long)strtol(buffer, NULL, 0);
        volatile long *point = (long *)address;
        *point = value;
        puts("done!");
    }
        return 0;
}