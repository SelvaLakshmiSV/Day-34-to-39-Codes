#include<stdio.h>
int fun(int,int);
int main()
{
    int a = 30,b = 20;
    fun(a,b);
    printf(" a is %d\n",a);
    printf(" b is %d\n",b);
    return 0;
}
fun(int a,int b)
{
    a = 20;
    b = 30;
}
