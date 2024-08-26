#include<stdio.h>
int main()
{
    char a;
    int m;
    int n;
    printf("Enter the operand");
    scanf("%c",&a);
    printf("Enter the first number \n");
    scanf("%d",&m);
    printf("Enter the second number \n");
    scanf("%d",&n);
    switch(a)
    {
        case '+':
        {
            printf("%d\n",m+n);
            break;
        }
        case '-':
        {
            printf("%d\n",m-n);
            break;
        }
        case '*':
        {
            printf("%d\n",m*n);
            break;
        }
        case '/':
        {
            printf("%d\n",m/n);
            break;
        }
        case '%':
        {
            printf("%d\n",m%n);
            break;
        }
        default:
        {
            printf("No function ");
        }
    }
}