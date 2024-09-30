#include <stdio.h>

int main()
{
    printf("Hello World");
    int a=6,b=7,c=8;
    
    a=a++ + ++a + b++;
    b=++b + c++ + c++;
    c=++a + ++b + ++c;
    printf("%d %d %d",a,b,c);

    return 0;
}