#include <stdio.h>
#include <stdlib.h>
int push(int a[], int n, int size, int top)
{
    if (top == size - 1)
    {
        printf("overflow\n");
    }
    else
    {
        top++;
        n++;
        int ele;
        printf("enter element:");
        scanf("%d", &ele);
        a[top] = ele;
    }
    for (int i = top; i >= 0; i--)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
    return top;
}
int pop(int a[], int top)
{
    if (top == -1)
    {
        printf("underflow\n");
    }
    else
    {
        top--;
    }
    for (int i = top; i >= 0; i--)
    {
        printf("%d ", a[i]);
    }
     printf("\n");
    return top;
}
void show(int a[], int top)
{
    for (int i = top; i >= 0; i--)
    {
        printf("%d ", a[i]);
    }
     printf("\n");
}
int main()
{
    int n, size, a[100], ch, top = -1;
    printf("enter no of size:");
    scanf("%d", &size);
    printf("enter no of terms:");
    scanf("%d", &n);
    printf("enter the element of array:");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        top++;
    }
    while (1)
    {
        printf("choices\n1)push\n2)pop\n3)show\n4)exit\n");
        printf("enter the choice:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            top=push(a, n, size, top);
            break;
        case 2:
            top=pop(a, top);
            break;
        case 3:
            show(a, top);
            break;
        case 4:
        printf("exiting....");
            exit(0);
        default:
            printf("invalid input\n");
            break;
        }
    }
    return 0;
}