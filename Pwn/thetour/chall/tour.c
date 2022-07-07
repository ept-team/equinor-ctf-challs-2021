#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <signal.h>
#include <unistd.h>

void * ptr;

void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
    if (sig == SIGALRM) {
        printf("[!] Anti DoS Signal. Patch me out for testing.");
        exit(0);
    }
}

void ignore_me_init_signal() {
    signal(SIGALRM, kill_on_timeout);
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
void move(long *addr) {
    puts("How far do you want to move?");
    unsigned int num = 0;
    scanf("%d", &num);
    (*addr) = (*addr +  num) % 0x4000;
    puts("done.");

}

void readAndPrint(uint8_t * addr){

    printf("%s", "data: ");
    for (int i = 0; i < 8; i++) {
        printf("%02x",addr[i]);
    }
    puts("");
}

void writeData(long * addr){
    long unsigned int data = 0;
    puts("gief data:");
    scanf("%lx", &data);
    (*addr) = data;
}
int main() {
    ignore_me_init_buffering();
    ignore_me_init_signal();
    seedRand();
    // printf("%p\n", &ptr);
    long base = (long) &main ;
    base -= 0x683;
    long randAddr = (rand() % 0x1000);
    int readsLeft = 5;
    int writesLeft = 1;
    //printf("base @ %lx\n", base);
    int idx = 0;
    while(1) {
        printf("You are stranded in a random place. What do you want to do?\n1. Read 8 bytes [%d left]\n2. Write 8 bytes [%d left]\n3. Jump\n4. Exit\n > ", readsLeft, writesLeft);
        scanf("%d", &idx);
        switch(idx) {
            case 1:
                if (readsLeft > 0) {
                    readAndPrint((void *)(base + randAddr));
                    readsLeft--;
                } else {
                    puts("Sorry, you are all out of reads.");
                }
                break;
            case 2:
                if (writesLeft > 0) {
                    writeData((void *)(base + randAddr));
                    writesLeft--;
                } else {
                    puts("Sorry, you are all out of writes.");
                }
                break;
            case 3:
                move(&randAddr);
                break;
            case 4:
                exit(1);
        }
    }  
    // 
    // ptr = &ptr + (rand() % 0x4000);
    // printf("%lx\n", takeOne);
    // printf("%p\n", &ptr);
    return 0;
}