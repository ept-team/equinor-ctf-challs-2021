#include <sys/mman.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <signal.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>

#include <sys/utsname.h>
#include <seccomp.h>

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

void disableSyscalls() {
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_ALLOW);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(fork), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(vfork), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(mprotect), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(mmap), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(brk), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(munmap), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(mremap), 0);

    seccomp_load(ctx);

}

void *page;
void *addr;
size_t size;

void runShellcode(void* page){
    ((void(*)())page)();
}

void seedRand() {
    int byte_count = 4;
    char data[byte_count];
    FILE *fp;
    fp = fopen("/dev/urandom", "r");
    fread(&data, 1, byte_count, fp);
    fclose(fp);
    int seed = (data[3] << 24) | ((data[2] & 0xFF) << 16) | ((data[1] & 0xFF) << 8) | (data[0] & 0xFF);
    srand(seed);
}

int main(int argc, char **argv, char **envp) {
    ignore_me_init_buffering();
    ignore_me_init_signal();
    

    seedRand();
    addr = (void *) ((long)(rand() & 0xffffff) << 0xc);
    page = mmap((void *) addr, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANON, 0, 0);

    if (addr != page) { 
        printf("mmap() error");
        exit(1337);
    }
    puts("Welcome to the shellcoding challenges!");
    puts("This is level 5.");
    puts("The flag somewhere in /opt/flag");
    puts("Enter your shellcode, maximum 70 bytes. ");
    printf("> ");
    fflush(stdout); 
    size = read(0, page, 70);
    //close stdin
     fclose(stdin);
    // self modifying shellcode not allowed
    if ( mprotect( addr, 0x1000, PROT_READ|PROT_EXEC) < 0 ) {
          printf("mprotect() error");
          return 1337;
      }
   
    if (size < 1) {
            printf("Failed to receieve input");
            exit(1337);
    }
    disableSyscalls();
    runShellcode(page);
    return 0;
}
