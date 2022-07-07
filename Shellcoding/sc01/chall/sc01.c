#include <sys/mman.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <signal.h>
#include <stdbool.h>


void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void ignore_me_kill_on_timeout(int sig) {
    if (sig == SIGALRM) {
        printf("[!] Anti DoS Signal. Patch me out for testing.");
        _exit(0);
    }
}

void ignore_me_init_signal() {
    signal(SIGALRM, ignore_me_kill_on_timeout);
    alarm(60);
}

void *page;
void *addr;
size_t size;

void runShellcode(void* page){
    ((void(*)())page)();
}

int main(int argc, char **argv, char **envp)
{
    ignore_me_init_buffering();
    ignore_me_init_signal();


    addr = (void *) 0xdead000;
    page = mmap((void *) addr, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANON, 0, 0);

    if (addr != page) { 
        printf("mmap() error");
        exit(1337);
    }
    puts("Welcome to the shellcoding challenges!");
    puts("This is level 1.");
    puts("The flag is in /opt/flag");
    puts("Enter your shellcode, maximum 0x200 bytes. ");
    printf("> ");
    fflush(stdout); 
    size = read(0, page, 0x200);
    if (size < 1) {
            printf("Failed to receieve input");
            exit(1337);
    }

    runShellcode(page);
    

    return 0;
}
