#include <sys/mman.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <signal.h>
#include <stdbool.h>
#include <seccomp.h>
#define flaglength 50

void *page;
void *addr;
char flag[flaglength];
size_t size;

void disableSyscalls() {
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_ALLOW);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(fork), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(vfork), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(read), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(open), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(close), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(lseek), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(pread64), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(readv), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(pipe), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(sendfile), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(recvmsg), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(openat), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(readlinkat), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(faccessat), 0);
    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(tee), 0);


    seccomp_load(ctx);

}

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

void runShellcode(void* page){
    ((void(*)())page)();
}
int arrContains( void* value, void ** arr, int n )
{
    int i = 0;

    while ( i < n && arr[i] != value ) i++;
    return i != n;
}
void getFlag(char* addr) {
    int temp=0;

    FILE *fp; 
    char ch;
    fp = fopen ("/opt/flag", "r");
    int i = 0;
    while((ch = fgetc(fp)) != EOF) {
        addr[i] = ch;
        i++;
    }
    //our flag is on the heap, we need to clean it up.
    __asm__(
        "xor r15, r15;"
        "mov [rsi], r15;"
        "add rsi, 8;"
        "mov [rsi], r15;"
        "add rsi, 8;"
        "mov [rsi], r15;"
        "add rsi, 8;"
        "mov [rsi], r15;"
        "add rsi, 8;"
        "mov [rsi], r15;"
        "add rsi, 8;"
        "mov [rsi], r15;"
        "sub rsi, 0x28;"
    );
    fclose(fp);

}

int main(int argc, char **argv, char **envp) {
    ignore_me_init_buffering();
    ignore_me_init_signal();
    seedRand();

    addr = (void *) 0xdead000;
    page = mmap((void *) addr, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANON, 0, 0);

    if (addr != page) { 
        printf("mmap() error");
        exit(1337);
    }

    void *ptrArr[100];
    void *temp, *temp2;
    const int N = sizeof( ptrArr ) / sizeof( *ptrArr );

    for (int i = 0; i < 100; i++) {
        temp = (void *) ((long)(rand() & 0xffffff) << 0xc);

        if (!arrContains( temp, ptrArr, i )) {
            ptrArr[i] = temp;
            temp2 = mmap((void *) temp, 0x1000, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANON, 0, 0);
            if (addr != page) { 
            printf("mmap() error");
            exit(1337);
            }
        }
        else {
            printf("errorz");
            exit(1337);
        }
    }


    void* flagaddr = (void*)((long)ptrArr[rand() % 100] |  rand() % (0x1000-flaglength));
    getFlag(flagaddr);
    flagaddr = 0;
    for(int i = 0; i < 100; i++) {
        ptrArr[i] = 0;
    }
    // rbx is pointing to the correct memory page, removing.
    __asm__ (
        "xor rbx, rbx;"
    );

    puts("Welcome to the shellcoding challenges!");
    puts("This is level 4.");
    puts("The flag is somewhere in memory, find it!");
    puts("Enter your shellcode, maximum 100 bytes. ");
    printf("> ");
    fflush(stdout); 
    size = read(0, page, 100);

    if (size < 1) {
            printf("Failed to receieve input");
            exit(1337);
    }

    if ( mprotect( addr, 0x1000, PROT_READ|PROT_EXEC) < 0 ) {
          printf("mprotect() error");
          exit(1337);
    }
   

    disableSyscalls();
    runShellcode(page);
    return 0;
}
