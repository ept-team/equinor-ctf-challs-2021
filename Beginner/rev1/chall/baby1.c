#include <stdio.h>
#include <string.h>

void decrypt(char *str2)
{
  int length=strlen(str2);
  for (int i=0; i<length; i++)
  {
    str2[i] = i+1 ^ str2[i];

  }
}

int main(){
  char str[] = "\x42\x6d\x76\x68\x61\x26\x7e\x67\x7c\x2a\x7b\x60\x68\x6f\x7c\x75\x31\x75\x7a\x62\x70\x36\x7a\x7d\x39\x7b\x3b\x7a\x71\x7f\x78\x1f";
  char str2[]  =  "\x44\x52\x57\x7f\x72\x67\x7e\x57\x7d\x65\x64\x53\x68\x6f\x75\x69\x6c";
  char buf[100];

  puts("Ask nicely and you actually might even get a flag :)");
  fgets(buf, 99, stdin);
  buf[strcspn(buf, "\n")] = 0;
  decrypt(str);
  if(strcmp(buf,str)==0) {
      decrypt(str2);
      puts(str2);
  }
  else {
      puts("I am sorry, but you didn't ask nice enough :(");
  }

  return 0;
}