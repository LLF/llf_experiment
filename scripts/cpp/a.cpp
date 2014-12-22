#include <iostream>
#include <stdio.h>

int main(){
    char words[20] = "ab cde 12 fgh";
    char * wordss = "ab cde 12 fgh";
    char str[4];
    int i;
    int d;
    sscanf(wordss+1, "%s %*s %x", str, &i);
    printf("%s,  %d\n", str, i);
    int b = ( i < 0);
    printf("%d", b);
}
