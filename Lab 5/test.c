#include <stdio.h>
#include <string.h>

void int2str(int a, char s[]) {
  int i = 0;
  char *p = s;

  while (a != 0) {

    i = a % 10;
    a /= 10;
    *p = i + '0';
    p++;
  }
  int x = sizeof(s);
  
  int y = sizeof(char);
  
  int length = (x/y)/2;
  
  for (int i = 0; i < length/2; i++) {
    char temp = s[i];
    s[i] = s[length-1-i];
    s[length-1-i] = temp;
  }
  
}

int main() {
  char ns[11];
  int2str(1234,ns);
  printf("%s",ns);
}
