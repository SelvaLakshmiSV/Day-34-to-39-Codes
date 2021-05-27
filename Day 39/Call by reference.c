#include<stdio.h>
fun(int *ptr1,int *ptr2){
    *ptr1 = 20;
    *ptr2 = 30;
}
int main()
{
    int a = 30,b = 20;
    fun(&a,&b);
    printf(" a is %d\n",a);
    printf(" b is %d\n",b);
    return 0;
}

